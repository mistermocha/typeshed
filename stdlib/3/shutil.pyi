# Stubs for shutil
import os
import sys

# Based on http://docs.python.org/3.2/library/shutil.html

# 'bytes' paths are not properly supported: they don't work with all functions,
# sometimes they only work partially (broken exception messages), and the test
# cases don't use them.

from typing import (
    List, Iterable, Callable, Any, Tuple, Sequence, NamedTuple, IO,
    AnyStr, Optional, Union
)

if sys.version_info >= (3, 6):
    _Path = Union[str, os.PathLike[str]]
    # Return value of some functions that may either return a path-like object that was passed in or
    # a string
    _PathReturn = Any
else:
    _Path = str
    _PathReturn = str

def copyfileobj(fsrc: IO[AnyStr], fdst: IO[AnyStr],
                length: int = ...) -> None: ...


if sys.version_info >= (3, 3):
    def copyfile(src: _Path, dst: _Path, *,
                 follow_symlinks: bool = ...) -> _PathReturn: ...
    def copymode(src: _Path, dst: _Path, *,
                 follow_symlinks: bool = ...) -> None: ...
    def copystat(src: _Path, dst: _Path, *,
                 follow_symlinks: bool = ...) -> None: ...
    def copy(src: _Path, dst: _Path, *,
             follow_symlinks: bool = ...) -> _PathReturn: ...
    def copy2(src: _Path, dst: _Path, *,
              follow_symlinks: bool = ...) -> _PathReturn: ...
else:
    def copyfile(src: _Path, dst: _Path) -> None: ...
    def copymode(src: _Path, dst: _Path) -> None: ...
    def copystat(src: _Path, dst: _Path) -> None: ...
    def copy(src: _Path, dst: _Path) -> None: ...
    def copy2(src: _Path, dst: _Path) -> None: ...

def ignore_patterns(*patterns: _Path) -> Callable[[_Path, List[str]],
                                                  Iterable[str]]: ...

_IgnoreFn = Union[None, Callable[[str, List[str]], Iterable[str]], Callable[[_Path, List[str]], Iterable[str]]]
if sys.version_info >= (3, 3):
    def copytree(src: _Path, dst: _Path, symlinks: bool = ...,
                 ignore: _IgnoreFn = ...,
                 copy_function: Callable[[str, str], None] = ...,
                 ignore_dangling_symlinks: bool = ...) -> _PathReturn: ...
else:
    def copytree(src: str, dst: str, symlinks: bool = ...,
                 ignore: _IgnoreFn = ...,
                 copy_function: Callable[[str, str], None] = ...,
                 ignore_dangling_symlinks: bool = ...) -> None: ...

def rmtree(path: _Path, ignore_errors: bool = ...,
           onerror: Callable[[Any, Any, Any], None] = ...) -> None: ...

if sys.version_info >= (3, 5):
    def move(src: _Path, dst: _Path,
             copy_function: Union[Callable[[str, str], None], Callable[[_Path, _Path], None]] = ...) -> _PathReturn: ...
elif sys.version_info >= (3, 3):
    def move(src: _Path, dst: _Path) -> str: ...
else:
    def move(src: _Path, dst: _Path) -> None: ...

if sys.version_info >= (3, 3):
    _ntuple_diskusage = NamedTuple('usage', [('total', int),
                                             ('used', int),
                                             ('free', int)])
    def disk_usage(path: _Path) -> _ntuple_diskusage: ...
    def chown(path: _Path, user: Optional[str] = ...,
              group: Optional[str] = ...) -> None: ...
    def which(cmd: _Path, mode: int = ...,
              path: Optional[_Path] = ...) -> Optional[str]: ...

class Error(Exception): ...
if sys.version_info >= (3, 4):
    class SameFileError(Error): ...

def make_archive(base_name: str, format: str, root_dir: _Path = ...,
                 base_dir: _Path = ..., verbose: bool = ...,
                 dry_run: bool = ..., owner: str = ..., group: str = ...,
                 logger: Any = ...) -> str: ...
def get_archive_formats() -> List[Tuple[str, str]]: ...

# TODO function is a callback that receives keyword arguments; should make it not use Any
# once we have support for callable types with keyword args
def register_archive_format(name: str, function: Any,
                            extra_args: Sequence[Tuple[str, Any]] = ...,
                            description: str = ...) -> None: ...
def unregister_archive_format(name: str) -> None: ...
# Should be _Path once http://bugs.python.org/issue30218 is fixed
def unpack_archive(filename: str, extract_dir: _Path = ...,
                   format: str = ...) -> None: ...
def register_unpack_format(name: str, extensions: List[str], function: Any,
                           extra_args: Sequence[Tuple[str, Any]] = ...,
                           description: str = ...) -> None: ...
def unregister_unpack_format(name: str) -> None: ...
def get_unpack_formats() -> List[Tuple[str, List[str], str]]: ...

if sys.version_info >= (3, 3):
    def get_terminal_size(fallback: Tuple[int, int] = ...) -> os.terminal_size: ...
