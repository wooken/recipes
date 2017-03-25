#!/usr/bin/env python

from jinja2 import FileSystemLoader, Environment
import pytoml as toml


def load_template(filename):
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
    return env.get_template(filename)


def main():
    with open('data/slow-cooked-chili.toml') as f:
        data = toml.load(f)
    template = load_template('recipe.md.py')
    output = template.render(
        d=data,
    )
    with open('harro.md', 'w') as f:
        f.write(output)

if __name__ == "__main__":
    main()
