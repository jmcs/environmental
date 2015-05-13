[![Latest Version](https://pypip.in/version/zalando-turnstile/badge.svg)](https://pypi.python.org/pypi/environmental)
[![Development Status](https://pypip.in/status/environmental/badge.svg)](https://pypi.python.org/pypi/environmental)
[![License](https://img.shields.io/pypi/l/environmental.svg)](https://github.com/zalando/environmental/blob/master/LICENSE)

environmental
=============
Map a python configuration from environment variables.

Overview
--------
**environmental** allows you to map class properties to environment variables.

By using  **environmental** you can keep your configuration in a single class your IDE understands and have convenient
and safe type conversions between the strings stored in your environment and python types.

The created properties are also writable so if you assign to them they will change on your environment and will be
available to your child processes.

Example
-------
```python
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
```

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
