from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MissileApproachingRequest(_message.Message):
    __slots__ = ["x_coordinate", "y_coordinate"]
    X_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    Y_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    x_coordinate: int
    y_coordinate: int
    def __init__(self, x_coordinate: _Optional[int] = ..., y_coordinate: _Optional[int] = ...) -> None: ...

class MissileApproachingReply(_message.Message):
    __slots__ = ["x_coordinate", "y_coordinate"]
    X_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    Y_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    x_coordinate: int
    y_coordinate: int
    def __init__(self, x_coordinate: _Optional[int] = ..., y_coordinate: _Optional[int] = ...) -> None: ...

class SoldierReadyRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
