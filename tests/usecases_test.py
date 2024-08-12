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

from __future__ import annotations

from typing import Any
from grscheller.untyped.nothing import Nothing, nothing  # type: ignore

def add2(x: int|Nothing) -> int:
    return x + 2

def make_non_negative(x: int|Nothing) -> int|Nothing:
    if x >= 0:
        return x
    if x < 0:
        return 0
    return nothing

def not_nothing(x: object) -> bool:
    if x is nothing:
        return False
    else:
        return True

class Test_Builtin_Containers:
    def test_mixed_list(self) -> None:
        foo: list[int|Nothing] = [23, -5, nothing, nothing, -1, 40]

        bar: list[int|Nothing] = list(map(add2, foo))
        assert bar == [25, -3, nothing, nothing, 1, 42]

        baz: list[int|Nothing] = []
        for x in foo:
            baz.append(make_non_negative(x))
        assert baz == [23, 0, nothing, nothing, 0, 40]

        fuz = list(filter(not_nothing, foo))
        assert fuz == [23, -5, -1, 40]

        zud1 = list(filter(None, foo))
        zud2 = list(filter(None, baz))
        assert zud1 == [23, -5, -1, 40]
        assert zud2 == [23, 40]
