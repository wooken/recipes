#!/usr/bin/env python
import os

from jinja2 import FileSystemLoader, Environment
import pytoml as toml


def load_template(filename):
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
    return env.get_template(filename)


def main():
    files = []
    readme_list = []
    for (dirpath, dirnames, filenames) in os.walk('data'):
        files.extend(filenames)
    for filename in files:
        basename_ext = os.path.splitext(filename)
        if basename_ext[1] == '.toml':
            with open('data/' + filename) as f:
                data = toml.load(f)
            template = load_template('templates/recipe.md.py')
            output = template.render(
                d=data,
            )
            recipe_path = 'recipe_files/' + basename_ext[0] + '.md'
            with open(recipe_path, 'w') as f:
                f.write(output)
            readme_list.append((data['title'], recipe_path))
    if readme_list:
        lines = []
        lines.append('# Recipes\n\n')
        for item in sorted(readme_list):
            lines.append('[' + item[0] + '](' + item[1] + ')\n')
        with open('README.md', 'w') as f:
            for line in lines:
                f.write(line)


if __name__ == "__main__":
    main()
