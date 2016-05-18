from setuptools import setup


setup(
    name='cmsplugin-biography',
    version='0.0.1',
    packages=['cmsplugin_biography', 'cmsplugin_biography.migrations', ],
    install_requires=[
        'django-cms',
        'djangocms-text-ckeditor==1.0.9',
        'easy-thumbnails==1.2',
    ],
    author='Kevin Richardson',
    author_email='kevin@magically.us',
    description='A Django CMS plugin that manages and displays biographical information',
    long_description=open('README.rst').read(),
    license='MIT',
    url='http://github.com/kfr2/cmsplugin-biography',
    include_package_data=True,
    zip_safe=False
)
