# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: grpcoauth/v1/user.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'grpcoauth/v1/user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17grpcoauth/v1/user.proto\x12\x0cgrpcoauth.v1\x1a\x1b\x62uf/validate/validate.proto\"\xd0\x01\n\x04User\x12%\n\x02id\x18\x01 \x01(\tB\x15\xbaH\x12r\x10\x32\x0e^[a-z0-9]{24}$R\x02id\x12\x1d\n\x04name\x18\x02 \x01(\tB\t\xbaH\x06r\x04\x10\x02\x18\x14R\x04name\x12?\n\x0cphone_number\x18\x03 \x01(\tB\x1c\xbaH\x19r\x17\x32\x15^010[0-9]{4}[0-9]{4}$R\x0bphoneNumber\x12#\n\x08nickname\x18\x04 \x01(\tB\x07\xbaH\x04r\x02\x18\x14R\x08nickname\x12\x1c\n\tthumbnail\x18\x05 \x01(\tR\tthumbnail\"7\n\x0eGetUserRequest\x12%\n\x02id\x18\x01 \x01(\tB\x15\xbaH\x12r\x10\x32\x0e^[a-z0-9]{24}$R\x02id\"9\n\x0fGetUserResponse\x12&\n\x04user\x18\x01 \x01(\x0b\x32\x12.grpcoauth.v1.UserR\x04user\";\n\x11\x43reateUserRequest\x12&\n\x04user\x18\x01 \x01(\x0b\x32\x12.grpcoauth.v1.UserR\x04user\"<\n\x12\x43reateUserResponse\x12&\n\x04user\x18\x01 \x01(\x0b\x32\x12.grpcoauth.v1.UserR\x04user\"-\n\x15GetUserByTokenRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\"@\n\x16GetUserByTokenResponse\x12&\n\x04user\x18\x01 \x01(\x0b\x32\x12.grpcoauth.v1.UserR\x04user\"3\n\x19GetUserListByTokenRequest\x12\x16\n\x06tokens\x18\x01 \x03(\tR\x06tokens\"F\n\x1aGetUserListByTokenResponse\x12(\n\x05users\x18\x01 \x03(\x0b\x32\x12.grpcoauth.v1.UserR\x05users2\xec\x02\n\x0bUserService\x12O\n\nCreateUser\x12\x1f.grpcoauth.v1.CreateUserRequest\x1a .grpcoauth.v1.CreateUserResponse\x12\x46\n\x07GetUser\x12\x1c.grpcoauth.v1.GetUserRequest\x1a\x1d.grpcoauth.v1.GetUserResponse\x12[\n\x0eGetUserByToken\x12#.grpcoauth.v1.GetUserByTokenRequest\x1a$.grpcoauth.v1.GetUserByTokenResponse\x12g\n\x12GetUserListByToken\x12\'.grpcoauth.v1.GetUserListByTokenRequest\x1a(.grpcoauth.v1.GetUserListByTokenResponseB\xaa\x01\n\x10\x63om.grpcoauth.v1B\tUserProtoP\x01Z:github.com/vet1ments/grpcoauth/go/grpcoauth/v1;grpcoauthv1\xa2\x02\x03GXX\xaa\x02\x0cGrpcoauth.V1\xca\x02\x0cGrpcoauth\\V1\xe2\x02\x18Grpcoauth\\V1\\GPBMetadata\xea\x02\rGrpcoauth::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpcoauth.v1.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.grpcoauth.v1B\tUserProtoP\001Z:github.com/vet1ments/grpcoauth/go/grpcoauth/v1;grpcoauthv1\242\002\003GXX\252\002\014Grpcoauth.V1\312\002\014Grpcoauth\\V1\342\002\030Grpcoauth\\V1\\GPBMetadata\352\002\rGrpcoauth::V1'
  _globals['_USER'].fields_by_name['id']._loaded_options = None
  _globals['_USER'].fields_by_name['id']._serialized_options = b'\272H\022r\0202\016^[a-z0-9]{24}$'
  _globals['_USER'].fields_by_name['name']._loaded_options = None
  _globals['_USER'].fields_by_name['name']._serialized_options = b'\272H\006r\004\020\002\030\024'
  _globals['_USER'].fields_by_name['phone_number']._loaded_options = None
  _globals['_USER'].fields_by_name['phone_number']._serialized_options = b'\272H\031r\0272\025^010[0-9]{4}[0-9]{4}$'
  _globals['_USER'].fields_by_name['nickname']._loaded_options = None
  _globals['_USER'].fields_by_name['nickname']._serialized_options = b'\272H\004r\002\030\024'
  _globals['_GETUSERREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_GETUSERREQUEST'].fields_by_name['id']._serialized_options = b'\272H\022r\0202\016^[a-z0-9]{24}$'
  _globals['_USER']._serialized_start=71
  _globals['_USER']._serialized_end=279
  _globals['_GETUSERREQUEST']._serialized_start=281
  _globals['_GETUSERREQUEST']._serialized_end=336
  _globals['_GETUSERRESPONSE']._serialized_start=338
  _globals['_GETUSERRESPONSE']._serialized_end=395
  _globals['_CREATEUSERREQUEST']._serialized_start=397
  _globals['_CREATEUSERREQUEST']._serialized_end=456
  _globals['_CREATEUSERRESPONSE']._serialized_start=458
  _globals['_CREATEUSERRESPONSE']._serialized_end=518
  _globals['_GETUSERBYTOKENREQUEST']._serialized_start=520
  _globals['_GETUSERBYTOKENREQUEST']._serialized_end=565
  _globals['_GETUSERBYTOKENRESPONSE']._serialized_start=567
  _globals['_GETUSERBYTOKENRESPONSE']._serialized_end=631
  _globals['_GETUSERLISTBYTOKENREQUEST']._serialized_start=633
  _globals['_GETUSERLISTBYTOKENREQUEST']._serialized_end=684
  _globals['_GETUSERLISTBYTOKENRESPONSE']._serialized_start=686
  _globals['_GETUSERLISTBYTOKENRESPONSE']._serialized_end=756
  _globals['_USERSERVICE']._serialized_start=759
  _globals['_USERSERVICE']._serialized_end=1123
# @@protoc_insertion_point(module_scope)
