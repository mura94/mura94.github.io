---
title: Display Sortable .csv Data in Markdown & Github
layout: post
---

<table>
{% for row = site.data.fragrances %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}

</table>