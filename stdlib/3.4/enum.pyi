import sys
from typing import List, Any, TypeVar, Union, Iterable, Iterator, TypeVar, Generic, Type, Sized, Reversible, Container, Mapping

_T = TypeVar('_T', bound=Enum)
_S = TypeVar('_S', bound=Type[Enum])

class EnumMeta(type, Iterable[Enum], Sized, Reversible[Enum], Container[Enum]):
    def __iter__(self: Type[_T]) -> Iterator[_T]: ...  # type: ignore
    def __reversed__(self: Type[_T]) -> Iterator[_T]: ...
    def __contains__(self, member: Any) -> bool: ...
    def __getitem__(self: Type[_T], name: str) -> _T: ...
    @property
    def __members__(self: Type[_T]) -> Mapping[str, _T]: ...

class Enum(metaclass=EnumMeta):
    def __new__(cls: Type[_T], value: Any) -> _T: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __dir__(self) -> List[str]: ...
    def __format__(self, format_spec: str) -> str: ...
    def __hash__(self) -> Any: ...
    def __reduce_ex__(self, proto: Any) -> Any: ...

    name = ...  # type: str
    value = ...  # type: Any

class IntEnum(int, Enum):
    value = ...  # type: int

def unique(enumeration: _S) -> _S: ...

if sys.version_info >= (3, 6):
    _auto_null = ...  # type: Any

    class auto(IntFlag):
        """auto: subclassing IntFlag so it picks up all implemented base functions, best modeling behavior of enum.auto()
        value = ...  # type: Any
        def __init__(self) -> None: ...

    class Flag(Enum):
        def __contains__(self: _T, other: _T) -> bool: ...
        def __repr__(self) -> str: ...
        def __str__(self) -> str: ...
        def __bool__(self) -> bool: ...
        def __or__(self: _T, other: _T) -> _T: ...
        def __and__(self: _T, other: _T) -> _T: ...
        def __xor__(self: _T, other: _T) -> _T: ...
        def __invert__(self: _T) -> _T: ...

    # All `type: ignore` comments below due to IntFlag making the function signatures more permissive.
    class IntFlag(int, Flag):  # type: ignore
        def __or__(self: _T, other: Union[int, _T]) -> _T: ...  # type: ignore
        def __and__(self: _T, other: Union[int, _T]) -> _T: ...  # type: ignore
        def __xor__(self: _T, other: Union[int, _T]) -> _T: ...  # type: ignore
        __ror__ = __or__
        __rand__ = __and__
        __rxor__ = __xor__
