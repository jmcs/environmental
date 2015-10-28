environmental
=============

.. image:: https://travis-ci.org/zalando/environmental.svg?branch=master
   :target: https://travis-ci.org/zalando/environmental
   :alt: Build Status


.. image:: https://coveralls.io/repos/zalando/environmental/badge.svg?branch=master
  :target: https://coveralls.io/r/zalando/environmental?branch=master
  :alt: Code Coverage

.. image:: https://img.shields.io/pypi/v/environmental.svg
   :target: https://pypi.python.org/pypi/environmental
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/environmental.svg
   :target: https://pypi.python.org/pypi/environmental
   :alt: Development Status

.. image:: https://img.shields.io/pypi/l/environmental.svg
   :target: https://github.com/zalando/environmental/blob/master/LICENSE
   :alt: License


Map a python configuration from environment variables.

Overview
--------
**environmental** allows you to map class properties to environment variables.

By using  **environmental** you can keep your configuration in a single class your IDE understands and have convenient
and safe type conversions between the strings stored in your environment and python types.

The created properties are also writable so if you assign to them they will change on your environment and will be
available to your child processes.

Installation
------------

.. code-block:: bash

    $ sudo pip3 install --upgrade environmental

Example
-------

.. code-block:: python

    import environmental
    import os

    class Configuration:
        port = environmental.Int('MY_APPLICATION_HTTP_PORT', 80)
        name = environmental.Str('MY_APPLICATION_NAME', 'Name')

    config = Configuration()
    config.port = 8080
    assert os.environ['MY_APPLICATION_HTTP_PORT'] == '8080'
    assert isinstance(os.environ['MY_APPLICATION_HTTP_PORT'], str)
    assert config.port == 8080
    assert isinstance(config.port, int)


Caveats
-------
Modifying mutable objects in the configuration (like lists) will not work:

.. code-block:: python

    import os, environmental
    class Configuration:
        list = environmental.List('LIST')

    os.environ['LIST'] = "[]"
    assert config.list == []
    config.list.append('test')
    assert config.list == []

But doing something that reassigns the variable will:

.. code-block:: python

    config.list += ['test']
    assert config.list == ['test']

License
-------
Copyright 2015 Zalando SE

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
