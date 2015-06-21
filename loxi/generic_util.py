# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution
"""
Utility functions independent of the protocol version
"""

# Automatically generated by LOXI from template generic_util.py
# Do not modify

import loxi
import struct

def pack_list(values):
    return "".join([x.pack() for x in values])

def unpack_list(reader, deserializer):
    """
    The deserializer function should take an OFReader and return the new object.
    """
    entries = []
    while not reader.is_empty():
        entries.append(deserializer(reader))
    return entries

def pad_to(alignment, length):
    """
    Return a string of zero bytes that will pad a string of length 'length' to
    a multiple of 'alignment'.
    """
    return "\x00" * ((length + alignment - 1)/alignment*alignment - length)

class OFReader(object):
    """
    Cursor over a read-only buffer

    OpenFlow messages are best thought of as a sequence of elements of
    variable size, rather than a C-style struct with fixed offsets and
    known field lengths. This class supports efficiently reading
    fields sequentially and is intended to be used recursively by the
    parsers of child objects which will implicitly update the offset.

    buf: buffer object
    start: initial position in the buffer
    length: number of bytes after start
    offset: distance from start
    """
    def __init__(self, buf, start=0, length=None):
        self.buf = buf
        self.start = start
        if length is None:
            self.length = len(buf) - start
        else:
            self.length = length
        self.offset = 0

    def read(self, fmt):
        st = struct.Struct(fmt)
        if self.offset + st.size > self.length:
            raise loxi.ProtocolError("Buffer too short")
        result = st.unpack_from(self.buf, self.start+self.offset)
        self.offset += st.size
        return result

    def read_all(self):
        s = self.buf[(self.start+self.offset):(self.start+self.length)]
        assert(len(s) == self.length - self.offset)
        self.offset = self.length
        return s

    def peek(self, fmt, offset=0):
        st = struct.Struct(fmt)
        if self.offset + offset + st.size > self.length:
            raise loxi.ProtocolError("Buffer too short")
        result = st.unpack_from(self.buf, self.start + self.offset + offset)
        return result

    def skip(self, length):
        if self.offset + length > self.length:
            raise loxi.ProtocolError("Buffer too short")
        self.offset += length

    def skip_align(self):
        new_offset = (self.offset + 7) / 8 * 8
        if new_offset > self.length:
            raise loxi.ProtocolError("Buffer too short")
        self.offset = new_offset

    def is_empty(self):
        return self.offset == self.length

    # Used when parsing objects that have their own length fields
    def slice(self, length, rewind=0):
        if self.offset + length - rewind > self.length:
            raise loxi.ProtocolError("Buffer too short")
        reader = OFReader(self.buf, self.start + self.offset - rewind, length)
        reader.skip(rewind)
        self.offset += length - rewind
        return reader
