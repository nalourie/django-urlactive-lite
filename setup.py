import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-urlactive-lite',
    version='0.1',
    packages=['urlactive', 'urlactive.templatetags'],
    include_package_data=True,
    install_requires='django >= 1.6',
    license='MIT License',
    description='An example django template tag library for adding an "active" class to navigation links.',
    long_description=README,
    maintainer="Nick Lourie",
    maintainer_email="developer@nicholaslourie.com",
    keywords = "django navigation active templatetags",
    url='https://github.com/nalourie/django-urlactive-lite',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

