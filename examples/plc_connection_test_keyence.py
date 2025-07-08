#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plcpy.plc_interface_keyence import PLCInterfaceKeyence


plc = PLCInterfaceKeyence('192.168.0.10')
plc.open()
