
{% extends "mail_templated/base.tpl" %}
{% block subject %}
Verification Message
{% endblock %}

{% block body %}
Please Click on link blow:
{% endblock %}

{% block html %}
<p> your new password: {{password}} </p>
{% endblock %}