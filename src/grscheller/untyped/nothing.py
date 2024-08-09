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

"""A nothing is an attempt to give Python a "bottom" type.

* unlike a true bottom, it can be instantiated as a singleton
* types like `~T|None` and `~T|()` act like a poor man's Optional/Maybe Monad
  * both None and () make for lousy bottom types
  * both don't accept many methods, None has no length, at least () is iterable
  * both must constantly be checked for when returned from functions
  * many developers will None and () as sentinel values
"""

from __future__ import annotations

__all__ = [ 'Nothing', 'nothing' ]
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2023-2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"

from typing import Any, Callable, Iterator, Optional
from collections import namedtuple

_Nothing_Nada = namedtuple('_Nothing_Nada', 'x')
_nada = _Nothing_Nada(None)

class Nothing():
    """
    #### Singleton semantically represents a missing value.

    * nothing: Nothing = Nothing() is a singleton representing an absent value
    * makes for a better "bottom type" than either None or ()
      * returns itself for arbitrary method calls
      * returns itself if called as a Callable with arbitrary arguments
      * interpreted as an empty container by standard Python functions
      * for comparison operators return `False` to "stop an action"
        * behaves like IEEE Float NAN's with comparison operators
        * avoid using else clauses when comparing ~T|Nothing values
        * when on left:
          * always returns `False`
        * when on right:
          * relies on the "std convention" of returning `False` if types differ
          * avoid using `~T|Nothing` values on right side of comparisons
            * especially for numerical comparisons
    """
    __slots__ = ()

    def __new__(cls) -> Nothing:
        if not hasattr(cls, 'instance'):
            cls.instance = super(Nothing, cls).__new__(cls)
        return cls.instance

    def __iter__(self) -> Iterator[Any]:
        return iter(())

    def __repr__(self) -> str:
        return 'nothing'

    def __bool__(self) -> bool:
        return False

    def __len__(self) -> int:
        return 0

    def __add__(self, right: Any) -> Any:
        return Nothing()

    def __radd__(self, left: Any) -> Any:
        return Nothing()

    def __mul__(self, right: Any) -> Any:
        return Nothing()

    def __rmul__(self, left: Any) -> Any:
        return Nothing()

    def __ge__(self, right: Any) -> bool:
        return False

    def __gt__(self, right: Any) -> bool:
        return False

    def __le__(self, right: Any) -> bool:
        return False

    def __lt__(self, right: Any) -> bool:
        return False

    def __eq__(self, right: Any) -> bool:
        return False

    def __ne__(self, right: Any) -> bool:
        return False

    def __getitem__(self, index: int|slice) -> Any:
        return Nothing()

    def __setitem__(self, index: int|slice, item: Any) -> None:
        return

    def __call__(*args: Any, **kwargs: Any) -> Any:
        return Nothing()

    def __getattr__(self, name: str) -> Callable[[Any], Any]:
        """Commented out for doc generation, pdoc gags on this method."""
        def method(*args: Any, **kwargs: Any) -> Any:
            return Nothing()
        return method

    def get(self, alt: Optional[Any]=_nada) -> Any:
        """Returns an alternate value, defaults Nothing()."""
        if alt == _nada:
            return Nothing()
        else:
            return alt

nothing = Nothing()
