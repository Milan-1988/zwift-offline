# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: per-session-info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16per-session-info.proto\">\n\nTcpAddress\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\n\n\x02\x66\x33\x18\x03 \x01(\x05\x12\n\n\x02\x66\x34\x18\x04 \x01(\x05\"\'\n\tTcpConfig\x12\x1a\n\x05nodes\x18\x01 \x03(\x0b\x32\x0b.TcpAddress\"A\n\x0cPartnersUrls\x12\x16\n\x0etodaysplan_url\x18\x01 \x01(\t\x12\x19\n\x11trainingpeaks_url\x18\x02 \x01(\t\"\x81\x01\n\x0ePerSessionInfo\x12\x11\n\trelay_url\x18\x01 \x02(\t\x12\x1b\n\x04\x61pis\x18\x02 \x01(\x0b\x32\r.PartnersUrls\x12\x0c\n\x04time\x18\x03 \x01(\x04\x12\x19\n\x05nodes\x18\x04 \x01(\x0b\x32\n.TcpConfig\x12\x16\n\x0emaxSegmSubscrs\x18\x05 \x01(\x05')



_TCPADDRESS = DESCRIPTOR.message_types_by_name['TcpAddress']
_TCPCONFIG = DESCRIPTOR.message_types_by_name['TcpConfig']
_PARTNERSURLS = DESCRIPTOR.message_types_by_name['PartnersUrls']
_PERSESSIONINFO = DESCRIPTOR.message_types_by_name['PerSessionInfo']
TcpAddress = _reflection.GeneratedProtocolMessageType('TcpAddress', (_message.Message,), {
  'DESCRIPTOR' : _TCPADDRESS,
  '__module__' : 'per_session_info_pb2'
  # @@protoc_insertion_point(class_scope:TcpAddress)
  })
_sym_db.RegisterMessage(TcpAddress)

TcpConfig = _reflection.GeneratedProtocolMessageType('TcpConfig', (_message.Message,), {
  'DESCRIPTOR' : _TCPCONFIG,
  '__module__' : 'per_session_info_pb2'
  # @@protoc_insertion_point(class_scope:TcpConfig)
  })
_sym_db.RegisterMessage(TcpConfig)

PartnersUrls = _reflection.GeneratedProtocolMessageType('PartnersUrls', (_message.Message,), {
  'DESCRIPTOR' : _PARTNERSURLS,
  '__module__' : 'per_session_info_pb2'
  # @@protoc_insertion_point(class_scope:PartnersUrls)
  })
_sym_db.RegisterMessage(PartnersUrls)

PerSessionInfo = _reflection.GeneratedProtocolMessageType('PerSessionInfo', (_message.Message,), {
  'DESCRIPTOR' : _PERSESSIONINFO,
  '__module__' : 'per_session_info_pb2'
  # @@protoc_insertion_point(class_scope:PerSessionInfo)
  })
_sym_db.RegisterMessage(PerSessionInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TCPADDRESS._serialized_start=26
  _TCPADDRESS._serialized_end=88
  _TCPCONFIG._serialized_start=90
  _TCPCONFIG._serialized_end=129
  _PARTNERSURLS._serialized_start=131
  _PARTNERSURLS._serialized_end=196
  _PERSESSIONINFO._serialized_start=199
  _PERSESSIONINFO._serialized_end=328
# @@protoc_insertion_point(module_scope)
