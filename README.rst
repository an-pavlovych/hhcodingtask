HH Coding Task
==============

This is Hunted Hive coding task.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

The task
========

Summary
-------
Your task is to create a django model that would store any data (based on a priori defined data scheme) and make this model usable across the project (admin integration + simple form view for adding new instances).

Requirements
------------
- django model, say `GenericModel`, that stores any data (proposed aproach is to use JSON field but we're open to better solutions)
- come up with a scheme describing data that `GenericModel` can store/process, for simplicity let's store it as a project-wide setting. Scheme can support only basic data types, like number, strings etc.
- view with form for end users for adding new instances of the `GenericModel` with appropriate validation. Example: if scheme declares we have "age" field that is of "integer" type, putting text in the form field will cause validation error with relevant message for end users
- django admin integration so admin can view/edit `GenericModel` instances

How to set up this project?
===========================
The project has been built using cookiecutter-django template (https://github.com/pydanny/cookiecutter-django). Please refer to its docs for some more information. Launching the project follows well known guidelines of setting up a standard django project:

- creating virtualenv
- installing requirements
- running migrations
- running django dev server

Collaboration
=============
Please create a separate branch where you can commit your work. Follow general guidelines of keeping git history clean and use meaningful messages. Once you're done, please create a pull request where you can describe your solution.
