#!/usr/bin/python

from bitstring import BitArray 
import struct

class RTP(object):
	FALSE = '0b0'
	TRUE = '0b1'
	ZERO2 = '0b00'
	ONE2 = '0b01'
	TWO2 = '0b10'
	THREE2 = '0b11'
	
	def __init__(self, *args, **kwargs):
		self.version = kwargs.get('version')
		self.padding = kwargs.get('padding')
		self.extension = kwargs.get('extension')
		self.csrc_count = kwargs.get('csrc_count')
		self.marker = kwargs.get('marker')
		self.payload_type = kwargs.get('payload_type')
		self.seq_num = kwargs.get('seq_num')
		self.timestamp = kwargs.get('timestamp')
		self.ssrc = kwargs.get('ssrc')
		self.csrc = kwargs.get('csrc')

	def __str__(self):
		print("Printing out RTP values")
		print(self.get_version())
		print(self.get_padding())
		print(self.get_extension())
		print(self.get_csrc_count())
		print(self.get_marker())
		print(self.get_payload_type())
		print(self.get_seq_num())
		print(self.get_timestamp())
		print(self.get_ssrc())
		print(self.get_csrc())
		print("Done")
		return ""

	# TODO Do we need negatives? If so, this needs more testing.
	def bin_formater(self, value, length):
		if value is None:
			return ("0b" + bin(0).lstrip('-0b').zfill(length))
		else:
			return ("0b" + bin(value).lstrip('-0b').zfill(length))

	def bin_to_uint(self, value):
		return BitArray(bin=value).uint

	def bin_to_bool(self, value):
		return BitArray(bin=value).bool

	def to_bitarray(self):
		# Version is always 2
		ba = BitArray(self.TWO2)	
		ba.append(self.TRUE) if self.padding else ba.append(self.FALSE)
		ba.append(self.TRUE) if self.extension else ba.append(self.FALSE)
		ba.append(self.bin_formater(self.csrc_count, 4))
		ba.append(self.TRUE) if self.marker else ba.append(self.FALSE)
		ba.append(self.bin_formater(self.payload_type, 8))
		ba.append(self.bin_formater(self.seq_num, 16))
		ba.append(self.bin_formater(self.timestamp, 32))
		ba.append(self.bin_formater(self.ssrc, 32))
		ba.append(self.bin_formater(self.csrc, 32))
		return ba

	# TODO Currently sets each field to a bitstring. 
	#      Should convert to actual values
	def from_bitarray(self, ba):
		bas = ba.bin
		self.set_version(bas[0:2])
		self.set_padding(bas[2:3])
		self.set_extension(bas[3:4])
		self.set_csrc_count(bas[4:8])
		self.set_marker(bas[8:9])
		self.set_payload_type(bas[9:16])
		self.set_seq_num(bas[16:32])
		self.set_timestamp(bas[32:64])
		self.set_ssrc(bas[64:96])
		self.set_csrc(bas[96:128])

	# Getters

	def get_version(self):
		return self.version

	def get_padding(self):
		return self.padding

	def get_extension(self):
		return self.extension

	def get_csrc_count(self):
		return self.csrc_count

	def get_marker(self):
		return self.marker

	def get_payload_type(self):
		return self.payload_type

	def get_seq_num(self):
		return self.seq_num

	def get_timestamp(self):
		return self.timestamp

	def get_ssrc(self):
		return self.ssrc

	def get_csrc(self):
		return self.csrc

	# Setters

	def set_version(self, v):
		self.version = bin_to_uint(v)

	def set_padding(self, p):
		self.padding = bin_to_bool(p)

	def set_extension(self, e):
		self.extension = bin_to_bool(e)

	def set_csrc_count(self, cc):
		self.csrc_count = bin_to_uint(cc)

	def set_marker(self, m):
		self.marker = bin_to_bool(m)

	def set_payload_type(self, pt):
		self.payload_type = bin_to_uint(pt)

	def set_seq_num(self, sn):
		self.seq_num = bin_to_uint(sn)

	# TODO add bin to timestamp conversion. Need format
	def set_timestamp(self, t):
		self.timestamp = t

	def set_ssrc(self, ss):
		self.ssrc = bin_to_uint(ss)

	def set_csrc(self, cs):
		self.csrc = bin_to_uint(cs)

