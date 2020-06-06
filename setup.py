import os

from setuptools import setup, find_packages


setup(name='etl',
      version='0.0',
      description='etl server',
      long_description='ETL RESTful server',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points="""\
      [paste.app_factory]
      main = etl:main
      [console_scripts]
      etl.worker = jobs.worker:worker
      """
      )
