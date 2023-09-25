from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MissileLaunchRequest(_message.Message):
    __slots__ = ["x_coordinate", "y_coordinate"]
    X_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    Y_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    x_coordinate: int
    y_coordinate: int
    def __init__(self, x_coordinate: _Optional[int] = ..., y_coordinate: _Optional[int] = ...) -> None: ...

class MissileLaunchReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GameDetailsReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GameDetailsRequest(_message.Message):
    __slots__ = ["N", "M", "T", "t"]
    N_FIELD_NUMBER: _ClassVar[int]
    M_FIELD_NUMBER: _ClassVar[int]
    T_FIELD_NUMBER: _ClassVar[int]
    T_FIELD_NUMBER: _ClassVar[int]
    N: int
    M: int
    T: int
    t: int
    def __init__(self, N: _Optional[int] = ..., M: _Optional[int] = ..., T: _Optional[int] = ..., t: _Optional[int] = ...) -> None: ...
