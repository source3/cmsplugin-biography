===================
cmsplugin-biography
===================

cmsplugin-biography is a `Django CMS`_ plugin that allows the user to create and refer to biographical information. For instance, you can create a biography of a keynote speaker and refer to the biography in multiple locations across a website. Currently, the plugin manages biographies of people.

.. _Django CMS: https://www.django-cms.org/

License
=======
This work is released under the MIT license. See ``LICENSE`` for more details.

Installation
============
1. Load your project's virtualenv.
2. Run ``pip install git+git://github.com/kfr2/cmsplugin-biography.git``.
3. Add 'cmsplugin_biography' and 'easy_thumbnails' to the ``INSTALLED_APPS`` setting.
4. Set ``THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE`` (or to your storage backend of choice) in ``settings.py``.
5. Run ``python manage.py syncdb`` or ``python manage.py migrate`` if you have South installed.

Configuration
=============

Thumbnail Sizes
---------------
easy-thumbnails accepts a `THUMBNAIL_ALIASES`_ setting that allows you to define your standard thumbnail sizes and options. The alias can then be referred to in the biography templates: ``{{ instance.image|thumbnail_url:'alias_name' }}``

.. _THUMBNAIL_ALIASES: http://easy-thumbnails.readthedocs.org/en/latest/usage/#thumbnail-aliases

Biography Templates
-------------------
If you would like to override the default person biography template, create your own version at ``(TEMPLATE_DIR)/cmsplugin_biography/person.html``. You will likely find the `existing template`_ useful as a reference.

.. _existing template: https://github.com/kfr2/cmsplugin-biography/blob/master/cmsplugin_biography/templates/cmsplugin_biography/person.html

Assumptions
===========
* `CKEditor`_ will be used on admin text fields via `djangocms-text-ckeditor`_
* `easy-thumbnails`_ will be used to create thumbnails of uploaded images.
* If you're using `django-cms-search`_, the rendered full text of the plugin will be added to the search index.

.. _CKEditor: http://ckeditor.com/
.. _djangocms-text-ckeditor: https://github.com/divio/djangocms-text-ckeditor
.. _easy-thumbnails: https://github.com/SmileyChris/easy-thumbnails
.. _django-cms-search: https://pypi.python.org/pypi/django-cms-search
