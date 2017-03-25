{# ex: set ft=jinja: #}
# {{ d.title }}
*[Source]({{ d.source }})*

| | |
|-|-|
| Prep time | {{ d.prep }}
| Cook time | {{ d.cook }}
| Yield | {{ d.yield }}

## Ingredients

{% for text in d.ingredients %}
- {{ text }}
{% endfor %}

## Directions

{% for text in d.directions %}
{{ loop.index }}. {{ text }}

{% endfor %}
