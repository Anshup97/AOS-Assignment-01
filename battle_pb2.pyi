from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCommanderReply(_message.Message):
    __slots__ = ["commanderId"]
    COMMANDERID_FIELD_NUMBER: _ClassVar[int]
    commanderId: str
    def __init__(self, commanderId: _Optional[str] = ...) -> None: ...

class GetCommanderRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class CommanderRequest(_message.Message):
    __slots__ = ["commanderId"]
    COMMANDERID_FIELD_NUMBER: _ClassVar[int]
    commanderId: str
    def __init__(self, commanderId: _Optional[str] = ...) -> None: ...

class CommanderReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class MissileLaunchedRequest(_message.Message):
    __slots__ = ["missile_type", "x_coordinate", "y_coordinate"]
    MISSILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    X_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    Y_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    missile_type: str
    x_coordinate: int
    y_coordinate: int
    def __init__(self, missile_type: _Optional[str] = ..., x_coordinate: _Optional[int] = ..., y_coordinate: _Optional[int] = ...) -> None: ...

class MissileLaunchedReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class MissileApproachingRequest(_message.Message):
    __slots__ = ["missile_type", "x_coordinate", "y_coordinate"]
    MISSILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    X_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    Y_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    missile_type: str
    x_coordinate: int
    y_coordinate: int
    def __init__(self, missile_type: _Optional[str] = ..., x_coordinate: _Optional[int] = ..., y_coordinate: _Optional[int] = ...) -> None: ...

class MissileApproachingReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SoldierIdRequest(_message.Message):
    __slots__ = ["soldierId"]
    SOLDIERID_FIELD_NUMBER: _ClassVar[int]
    soldierId: int
    def __init__(self, soldierId: _Optional[int] = ...) -> None: ...

class SoldierStatus(_message.Message):
    __slots__ = ["isAlive"]
    ISALIVE_FIELD_NUMBER: _ClassVar[int]
    isAlive: bool
    def __init__(self, isAlive: bool = ...) -> None: ...

class SoldierStatusAllRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SoldierStatusAllReply(_message.Message):
    __slots__ = ["statuses"]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    statuses: str
    def __init__(self, statuses: _Optional[str] = ...) -> None: ...

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

class GameDetailsReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GetGameDetailsRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GetGameDetailsReply(_message.Message):
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

class MatrixValues(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class MatrixRows(_message.Message):
    __slots__ = ["row"]
    ROW_FIELD_NUMBER: _ClassVar[int]
    row: _containers.RepeatedCompositeFieldContainer[MatrixValues]
    def __init__(self, row: _Optional[_Iterable[_Union[MatrixValues, _Mapping]]] = ...) -> None: ...

class Matrix(_message.Message):
    __slots__ = ["matrix"]
    MATRIX_FIELD_NUMBER: _ClassVar[int]
    matrix: _containers.RepeatedCompositeFieldContainer[MatrixRows]
    def __init__(self, matrix: _Optional[_Iterable[_Union[MatrixRows, _Mapping]]] = ...) -> None: ...

class MatrixRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
