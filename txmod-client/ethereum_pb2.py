# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethereum.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ethereum.proto',
  package='protoeth',
  syntax='proto3',
  serialized_options=b'\220\001\001',
  serialized_pb=b'\n\x0e\x65thereum.proto\x12\x08protoeth\"&\n\x0fTransactionInfo\x12\x13\n\x0btransaction\x18\x01 \x01(\t\"-\n\x08GetTxReq\x12\x11\n\tnetworkid\x18\x01 \x01(\r\x12\x0e\n\x06txhash\x18\x02 \x01(\t2T\n\x0fProtoEthService\x12\x41\n\x0eGetTransaction\x12\x12.protoeth.GetTxReq\x1a\x19.protoeth.TransactionInfo\"\x00\x42\x03\x90\x01\x01\x62\x06proto3'
)




_TRANSACTIONINFO = _descriptor.Descriptor(
  name='TransactionInfo',
  full_name='protoeth.TransactionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='protoeth.TransactionInfo.transaction', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=66,
)


_GETTXREQ = _descriptor.Descriptor(
  name='GetTxReq',
  full_name='protoeth.GetTxReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='networkid', full_name='protoeth.GetTxReq.networkid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txhash', full_name='protoeth.GetTxReq.txhash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['TransactionInfo'] = _TRANSACTIONINFO
DESCRIPTOR.message_types_by_name['GetTxReq'] = _GETTXREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransactionInfo = _reflection.GeneratedProtocolMessageType('TransactionInfo', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONINFO,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.TransactionInfo)
  })
_sym_db.RegisterMessage(TransactionInfo)

GetTxReq = _reflection.GeneratedProtocolMessageType('GetTxReq', (_message.Message,), {
  'DESCRIPTOR' : _GETTXREQ,
  '__module__' : 'ethereum_pb2'
  # @@protoc_insertion_point(class_scope:protoeth.GetTxReq)
  })
_sym_db.RegisterMessage(GetTxReq)


DESCRIPTOR._options = None

_PROTOETHSERVICE = _descriptor.ServiceDescriptor(
  name='ProtoEthService',
  full_name='protoeth.ProtoEthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=115,
  serialized_end=199,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTransaction',
    full_name='protoeth.ProtoEthService.GetTransaction',
    index=0,
    containing_service=None,
    input_type=_GETTXREQ,
    output_type=_TRANSACTIONINFO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROTOETHSERVICE)

DESCRIPTOR.services_by_name['ProtoEthService'] = _PROTOETHSERVICE

ProtoEthService = service_reflection.GeneratedServiceType('ProtoEthService', (_service.Service,), dict(
  DESCRIPTOR = _PROTOETHSERVICE,
  __module__ = 'ethereum_pb2'
  ))

ProtoEthService_Stub = service_reflection.GeneratedServiceStubType('ProtoEthService_Stub', (ProtoEthService,), dict(
  DESCRIPTOR = _PROTOETHSERVICE,
  __module__ = 'ethereum_pb2'
  ))


# @@protoc_insertion_point(module_scope)