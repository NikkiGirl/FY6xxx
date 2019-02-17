Help on module FY6xxx:

NAME
    FY6xxx

FILE
    /home/nikki/PycharmProjects/FY6xxx/FY6xxx.py

DESCRIPTION
    Module: FY6xxx  FeelElec FY6800 serial communication protocol library
    Version: 0.1
    Date: 17Feb2019
    Author: Nikki Cooper

    For documentation issue the following on the command line:
    pydoc FY6xxx

    Licensed under the GPL v3 by Nikki Cooper.

CLASSES
    __builtin__.object
	FY6800
	FY6XXX_Serial

    class FY6800(__builtin__.object)
     |	Methods defined here:
     |
     |	__init__(self, device=None, printsettings=None, muteexceptions=False, readtimeout=1, writetimeout=0.25)
     |	    Setup serial port the FY6800 is connected as and contains all the
     |	    necessary methods in order to read / write information to the FY6800
     |
     |	    :param device:	   string, Serial port device such as /dev/ttyUSB1
     |	    :param printsettings:  bool,   Print serial port parameters and exit program
     |	    :param muteexceptions: bool,   Mute printing of serial port exception errors to console
     |	    :param readtimeout:	   float,  Set the read data from serial device timeout in sec. def: 1 sec
     |	    :param writetimeout:   float,  Set the write data to serial device timeout in sec.	def: 0.25 sec
     |
     |	    :return   0:  Normal exit code
     |	    :return 255:  Error opening serial device
     |	    :return 254:  Error while reading or writing to / from serial device
     |	    :return 253:  Serial port device was not specified. Default: None
     |	    :return 252:  printsettings=True return code
     |
     |	    Example invocation: fy6800 = FY6xxx.FY6800("/dev/ttyUSB1")
     |				fy6800 = FY6XXX.FY6800(printsettings=True)
     |				fy6800 = FY6XXX.FY6800("/dev/ttyUSB1",muteexceptions=True)
     |				fy6800 = FY6XXX.FY6800("/dev/ttyUSB1", readtimeout=-0.80)
     |
     |	addSyncMode(self, syncobj)
     |	    Add synchronization mode
     |	    :param syncobj: string,  one of:
     |			    0 = Set Waveform of CH2 sync'ed with CH1
     |			    1 = Set Frequency of CH2 sync'ed with CH1
     |			    2 = Set Amplitude of CH2 sync'ed with CH1
     |			    3 = Set Offset of CH2 sync'ed with CH1
     |			    4 = Set Duty Cycle of CH2 sync'ed with CH1
     |	    :return: 0xa
     |	    NOTE: This function not available in sweep status
     |
     |	cancelSyncMode(self, syncobj)
     |	    Cancel synchronization mode
     |	    :param syncobj: string,  one of:
     |			    0 = Cancel Waveform of CH2 sync'ed with CH1
     |			    1 = Cancel Frequency of CH2 sync'ed with CH1
     |			    2 = Cancel Amplitude of CH2 channel sync'ed with CH1
     |			    3 = Cancel Offset of CH2 sync'ed with CH1
     |			    4 = Cancel Duty Cycle of CH2 sync'ed with CH1
     |	    :return: 0xa
     |
     |	getASKmode(self)
     |	    Read ASK modulation mode
     |	    :return:  integer, one of:
     |		      0 = Normal output without trigger
     |		      1 = Modulation mode of external signal input
     |		      2 = Manual modulation.
     |
     |	getBuzzerStatus(self)
     |	    Read the buzzer on/off status
     |	    :return: integer, 0 = disabled, 1 = enabled
     |
     |	getCh1Status(self)
     |	    Read the current enabled / disabled status of channel 1
     |	    :return: integer,  0 = disabled, 1 = enabled
     |
     |	getCh1Wave(self)
     |	    Read the current waveform for channel 1
     |	    :return: integer index value for self.waveForms
     |
     |	getCh1WaveAmplitude(self)
     |	    Read the amplitude of the waveform set in channel 1
     |	    :return: float, amplitude in volts
     |
     |	getCh1WaveDesc(self)
     |	    Read the  current waveform descriptor for channel 1
     |	    :return: string, key from self.waveForms
     |
     |	getCh1WaveDutyCycle(self)
     |	    Read channel 1 waveform duty cycle percentage
     |	    :return: float representing duty cycle in percent
     |
     |	getCh1WaveFreq(self)
     |	    Read the frequency of current waveform set in channel 1
     |	    :return: string.  The frequency in Hz
     |
     |	getCh1WaveOffset(self)
     |	    Read channel 1 waveform offset voltage
     |	    :return: float, offset voltage in volts.
     |
     |	getCh1WavePhase(self)
     |	    Read channel 1 waveform phase
     |	    :return: float,  the phase in degrees
     |
     |	getCh2Status(self)
     |	    Read the current enabled / disabled status of channel 2
     |	    :return: integer,  0 = disabled, 1 = enabled
     |
     |	getCh2Wave(self)
     |	    Read the current waveform for channel 1
     |	    :return: integer index value for self.waveForms
     |
     |	getCh2WaveAmplitude(self)
     |	    Read the amplitude of the waveform set in channel 2
     |	    :return: float, amplitude in volts
     |
     |	getCh2WaveDesc(self)
     |	    Read the current waveform descriptor for channel 2
     |	    :return: string, key from self.waveForms
     |
     |	getCh2WaveDutyCycle(self)
     |	    Read channel 2 waveform duty cycle percentage
     |	    :return: float representing duty cycle in percent
     |
     |	getCh2WaveFreq(self)
     |	    Read the frequency of current waveform set in channel 2
     |	    :return: string. The frequency in Hz
     |
     |	getCh2WaveOffset(self)
     |	    Read channel 2 waveform offset voltage
     |	    :return: float, offset voltage in volts.
     |
     |	getCh2WavePhase(self)
     |	    Read channel 2 waveform phase
     |	    :return: float,  the phase in degrees
     |
     |	getCounterCnt(self)
     |	    Read frequency counter count value.
     |	    :return: string, representing the count value.
     |
     |	getCounterCntPeriod(self)
     |	    Read frequency counter counting period.
     |	    :return: string, representing counting period in ns
     |
     |	getCounterDutyCycle(self)
     |	    Read frequency counter Duty Cycle.
     |	    :return: string, representing duty cycle in percent
     |
     |	getCounterFreq(self)
     |	    Read frequency counter frequency
     |	    :return: string, representing the frequency in Hz
     |
     |	getCounterGateTime(self)
     |	    Read frequency counter gate time.
     |	    :return: integer, one of:
     |		     0 =  1Sec
     |		     1 =  10sec
     |		     2 = 100sec
     |
     |	getCounterNegPulseWidth(self)
     |	    Read frequency counter Negative Pulse Width
     |	    :return: string, representing width of negative pulse in ns.
     |
     |	getCounterPosPulseWidth(self)
     |	    Read frequency counter Positive Pulse Width
     |	    :return: string, representing width of positive pulse in ns.
     |
     |	getFSKmode(self)
     |	    Read FSK modulation mode
     |	    :return:  integer, one of:
     |		      0 = Normal output without trigger
     |		      1 = Modulation mode of external signal input
     |		      2 = Manual modulation.
     |
     |	getFSKsecondaryFreq(self)
     |	    Read FSK secondary frequency.
     |	    :return: string, representing the FSK secondary frequency in Hz
     |
     |	getID(self)
     |	    Read serial number of the instrument
     |	    :return: string, instrument serial number
     |
     |	getModel(self)
     |	    Read model number of instrument
     |	    :return: string, model number of instrument.
     |
     |	getPSKmode(self)
     |	    Read PSK modulation mode
     |	    :return:  integer, one of:
     |		      0 = Normal output without trigger
     |		      1 = Modulation mode of external signal input
     |		      2 = Manual modulation.
     |
     |	getSyncInfo(self, syncobj)
     |	    Read synchronization information
     |	    :param syncobj: string, one of:
     |			     0 = Read Waveform sync info
     |			     1 = Read Frequency sync info
     |			     2 = Read Amplitude sync info
     |			     3 = Read Offset sync info
     |			     4 = Read Duty Cycle sync info
     |	    :return:  integer, one of:
     |			      0	  = disabled
     |			      255 = enabled
     |
     |	getTrigger(self)
     |	    Read trigger mode of channel 1 waveform.
     |	    :return:  integer,	one of:
     |		      0 = No trigger
     |		      1 = CH1 waveform triggered by CH2 waveform
     |		      2 = CH1 waveform triggered by ExT.in connector
     |		      3 = CH1 waveform triggered manually (one shot triggering)
     |
     |	getUplinkMode(self)
     |	    Read uplink mode.
     |	    :return:  integer:	0   = master
     |				255 = slave .
     |
     |	getUplinkStatus(self)
     |	    Read the uplink on/off status.
     |	    :return: integer, 0 = off, 1 = on
     |
     |	loadParams(self, position)
     |	    Load system configuration
     |	    :param position:  string, representing saved positions 01 - 20
     |	    :return: 0xa
     |
     |	pauseCounter(self, status)
     |	    Pause frequency counter measurement.
     |	    :param: status: string, one of:
     |			     0 = pause
     |			     1 = unpause
     |	    :return: string, one of:
     |		     current counter count if status = 0
     |		     0x0a = unpaused if status = 1.
     |
     |	readPulseTrigger(self)
     |	    Read pulse number of CH1 waveform
     |	    :return: string respresenting the pulse number.
     |
     |	resetCounterCnt(self)
     |	    Reset frequency counter count value.
     |	    :return: x0a
     |
     |	saveParams(self, position)
     |	    Save system configuration into position
     |	    :param position:  string respresnting position to save to 01 - 20
     |	    :return: 0xa
     |
     |	setASKmode(self, mode)
     |	    Set ASK modulation mode of CH1 waveform
     |	    :param mode: string, one of:
     |			 0 = Normal output without trigger
     |			 1 = Modulation mode of external signal input
     |			 2 = Manual modulation
     |	    :return: x0a
     |
     |	setBuzzerStatus(self, status)
     |	    Set buzzer on/off
     |	    :param status: bool, 0 = off, 1 = on
     |	    :return: x0a
     |
     |	setCh1Status(self, status)
     |	    Set the channel 1 enabled / disabled status
     |	    :param status: bool, 0 = disabled, 1 = enabled
     |	    :return: 0xa
     |
     |	setCh1Wave(self, waveindx)
     |	    Set the active waveform for channel 1
     |	    :param waveindx: integer.  Index to waveform  in self.waveForms
     |	    :return: 0xa
     |
     |	setCh1WaveAmplitude(self, amplitude)
     |	    Set the amplitude of the channel 1 waveform
     |	    :param amplitude: string in the form  of x.xx
     |	    :return:  0xa
     |
     |	setCh1WaveByKey(self, key)
     |	    Set the active waveform by key value
     |	    :param key:string defined in self.Ch1WaveForms
     |	    :return: 0xa
     |
     |	setCh1WaveDutyCycle(self, dcycle)
     |	    Set channel 1 waveform duty cycle percentage
     |	    :param dcycle: string in form of x.xx percent
     |	    :return: 0xa
     |
     |	setCh1WaveFreq(self, freq)
     |	    Set the waveform on channel 1
     |	    :param freq: 14 character string in Hz
     |	    :return: 0xa
     |
     |	setCh1WaveOffset(self, offset)
     |	    Set the channel 1 waveform offset voltage
     |	    :param offset: string in the form of x.xx
     |	    :return: 0xa
     |
     |	setCh1WavePhase(self, phase)
     |	    Set channel 1 waveform phase
     |	    :param phase: string in form of x.xx degrees
     |	    :return: 0xa
     |
     |	setCh1WavePulsePeriod(self, period)
     |	    Set the pulse period of the channel 1 waveform
     |	    :param period: string representing the period
     |	    :return: 0xa
     |
     |	setCh2Status(self, status)
     |	    Set the channel 2 enabled / disabled status
     |	    :param status: bool, 0 = disabled, 1 = enabled
     |	    :return: 0xa
     |
     |	setCh2Wave(self, waveindx)
     |	    Set the active waveform for channel 2
     |	    :param waveindx: integer. Index to waveform in self.waveForms
     |	    :return: 0xa
     |
     |	setCh2WaveAmplitude(self, amplitude)
     |	    Set the amplitude of the channel 2 waveform
     |	    :param amplitude: string in the form  of x.xx
     |	    :return:  0xa
     |
     |	setCh2WaveByKey(self, key)
     |	    Set the channel 2 active waveform by key value
     |	    :param key: string defined in self.Ch2WaveForms
     |	    :return: 0xa
     |
     |	setCh2WaveDutyCycle(self, dcycle)
     |	    Set channel 2 waveform duty cycle percentage
     |	    :param dcycle: string in form of x.xx percent
     |	    :return: 0xa
     |
     |	setCh2WaveFreq(self, freq)
     |	    Set the waveform on channel 2
     |	    :param freq: string, 14 characters in Hz
     |	    :return: 0xa
     |
     |	setCh2WaveOffset(self, offset)
     |	    Set the channel 2 waveform offset voltage
     |	    :param offset: string in the form of x.xx
     |	    :return: 0xa
     |
     |	setCh2WavePhase(self, phase)
     |	    Set channel 2 waveform phase
     |	    :param phase: string in form of x.xx degrees
     |	    :return: 0xa
     |
     |	setCounterCouplingMode(self, mode)
     |	    Set frequency counter coupling mode
     |	    :param mode: string, one of:
     |			 0 = DC coupling
     |			 1 = AC coupling
     |	    :return: x0a
     |
     |	setCounterGateTime(self, time)
     |
     |	setFSKmode(self, mode)
     |	    Set FSK modulation mode of CH1 waveform
     |	    :param mode: string, one of:
     |			 0 = Normal output without trigger
     |			 1 = Modulation mode of external signal input
     |			 2 = Manual modulation
     |	    :return: x0a
     |
     |	setFSKsecondaryFreq(self, freq)
     |	    Set secondary frequency of CH1 waveform FSK
     |	    :param freq: string, representing the FSK secondary frequency in Hz
     |	    :return: 0xa
     |
     |	setPSKmode(self, mode)
     |	    Set PSK modulation mode of CH1 waveform
     |	    :param mode: string, one of:
     |			 0 = Normal output without trigger
     |			 1 = Modulation mode of external signal input
     |			 2 = Manual modulation
     |	    :return: x0a
     |
     |	setPulseTrigger(self, pulseamt)
     |	    Set pulse number of CH1 waveform when triggered. Limits how many cycles
     |	    of the CH1 waveform will ouput.
     |	    :param pulseamt: string representing pulse number from 1 to 1048575
     |	    :return:
     |
     |	setSweepControlSource(self, source)
     |	    Set control source of sweep.
     |	    :param source: string, one of:
     |			   0 = control source is time
     |			   1 = control source is analog signal input from VCO IN terminal
     |	    :return: x0a
     |
     |	setSweepEndPos(self, data)
     |	    Set END position of sweep
     |	    :param data: string, depends on setting of obj in setSweepObject()
     |			  if obj is: 0, data = frequency in Hz
     |				     1, data = amplitude in Volts
     |				     2, data = offset in Volts
     |				     3, data = duty cycle in %
     |	    :return: x0a
     |
     |	setSweepMode(self, mode)
     |	    Set sweep mode.
     |	    :param mode: string, one of:
     |			 0 = Linear sweep
     |			 1 = Log sweep
     |	    :return: x0a
     |
     |	setSweepObject(self, obj)
     |	    Set object in sweep mode.
     |	    :param obj: string, one of:
     |			0 = set frequency to be object
     |			1 = set amplitude to be object
     |			2 = set offset to be object
     |			3 = set duty cycle to be object
     |	    :return:
     |
     |	setSweepStartPos(self, data)
     |	    Set START position of sweep
     |	    :param data: string, depends on setting of obj in setSweepObject()
     |			  if obj is: 0, data = frequency in Hz
     |				     1, data = amplitude in Volts
     |				     2, data = offset in Volts
     |				     3, data = duty cycle in %
     |	    :return: x0a
     |
     |	setSweepStatus(self, status)
     |	    Set sweep mode on/off
     |	    :param status: bool, one of:
     |			   0 = sweep turned off
     |			   1 = sweep turned on
     |	    :return: x0a
     |
     |	setSweepTime(self, time)
     |	    Set sweep time.
     |	    :param time: string, in form of xxx.xx
     |	    :return: x0a
     |
     |	setTrigger(self, triggersrc)
     |	    Set trigger mode of channel 1 waveform.
     |	    :triggersrc:   integer,  one of:
     |			    0 = Trigger disabled
     |			    1 = CH1 waveform triggered by CH2 waveform
     |			    2 = CH1 waveform triggered by ExT.in connector
     |			    3 = CH1 waveform triggered manually (one shot triggering)
     |				The CH1 waveform is triggered each time command is sent.
     |	    :return: x0a
     |
     |	setUplinkMode(self, mode)
     |	    Set uplink mode
     |	    :param mode: string, 0 = master, 1 = slave
     |	    :return: x0a
     |
     |	setUplinkStatus(self, status)
     |	    Set uplink on/off
     |	    :param status:  bool, 0 = off, 1 = on
     |	    :return: x0a
     |
     |	----------------------------------------------------------------------
     |	Data descriptors defined here:
     |
     |	__dict__
     |	    dictionary for instance variables (if defined)
     |
     |	__weakref__
     |	    list of weak references to the object (if defined)

    class FY6XXX_Serial(__builtin__.object)
     |	Methods defined here:
     |
     |	__del__(self)
     |
     |	__init__(self, device=None, muteexceptions=False, readtimeout=1, writetimeout=0.25)
     |	    Create a serial port object based on the FY6xxx device
     |	    :param device:	   string. Valid serial port such as "/dev/ttyUSB1"
     |	    :param muteexceptions: bool.  Mute serial port open / read / write exceptions.
     |
     |	close(self)
     |	    Closes the open serial port device
     |	    :return: None
     |
     |	flushinput(self)
     |	    flushes the serial input buffers
     |	    :return: None
     |
     |	read(self, size)
     |	    read size number of bytes from serial device
     |	    :param size: integer
     |	    :return:	 the data read from serial device
     |
     |	readline(self)
     |	    Read data from serial device until 1 of following occurs:
     |		1.  An 0xa (LF)is  detected in data stream
     |		2.  serial.timeout seconds has elapsed
     |	    serial.timeout can be adjusted by specifying readtimeout=
     |	    :return: The data read from serial device
     |
     |	write(self, cmd)
     |	    Write data to the serial device
     |	    :return: integer, if write timeout is configured for the port and the time is exceeded.
     |
     |	----------------------------------------------------------------------
     |	Data descriptors defined here:
     |
     |	__dict__
     |	    dictionary for instance variables (if defined)
     |
     |	__weakref__
     |	    list of weak references to the object (if defined)

DATA
    Ch1WaveForms = {'AM': '31', 'Adj Pulse': '03', 'CMOS': '02', 'Chirp': ...
    Ch2WaveForms = {'AM': '30', 'CMOS': '02', 'Chirp': '32', 'DC': '03', '...
    waveForms = ('Sine', 'Square', 'CMOS', 'Adj Pulse', 'DC', 'Triangle', ...

