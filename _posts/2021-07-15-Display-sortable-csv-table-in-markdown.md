---
layout: post
title: Display Sortable .csv Data in Markdown & Github
subtitle: test
datatable: true
---

# Test Heading

Test text


<table class = "display">

{% for row in site.assets.fragrances %}
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