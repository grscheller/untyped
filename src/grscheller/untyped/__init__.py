# Copyright 2023-2024 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
### Useful tools I found difficult to implement in a well typed manner.

#### class `Nothing()`

Singleton class representing a non-existent value.

* nothing = Nothing() is a singleton
* nothing should be compared with the `is` operator, not `==`
* more strict typing results in pdoc internal errors related to __getattr__

"""
__version__ = "0.0.0.2"
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"
