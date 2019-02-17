Help on module FY6xxx:

NNAAMMEE
    FY6xxx

FFIILLEE
    /home/nikki/PycharmProjects/FY6xxx/FY6xxx.py

DDEESSCCRRIIPPTTIIOONN
    Module: FY6xxx  FeelElec FY6800 serial communication protocol library
    Version: 0.1
    Date: 17Feb2019
    Author: Nikki Cooper
    
    For documentation issue the following on the command line:
    pydoc FY6xxx
    
    Licensed under the GPL v3 by Nikki Cooper.

CCLLAASSSSEESS
    __builtin__.object
        FY6800
        FY6XXX_Serial
    
    class FFYY66880000(__builtin__.object)
     |  Methods defined here:
     |  
     |  ____iinniitt____(self, device=None, printsettings=None, muteexceptions=False, readtimeout=1, writetimeout=0.25)
     |      Setup serial port the FY6800 is connected as and contains all the
     |      necessary methods in order to read / write information to the FY6800
     |      
     |      :param device:         string, Serial port device such as /dev/ttyUSB1
     |      :param printsettings:  bool,   Print serial port parameters and exit program
     |      :param muteexceptions: bool,   Mute printing of serial port exception errors to console
     |      :param readtimeout:    float,  Set the read data from serial device timeout in sec. def: 1 sec
     |      :param writetimeout:   float,  Set the write data to serial device timeout in sec.  def: 0.25 sec
     |      
     |      :return   0:  Normal exit code
     |      :return 255:  Error opening serial device
     |      :return 254:  Error while reading or writing to / from serial device
     |      :return 253:  Serial port device was not specified. Default: None
     |      :return 252:  printsettings=True return code
     |      
     |      Example invocation: fy6800 = FY6xxx.FY6800("/dev/ttyUSB1")
     |                          fy6800 = FY6XXX.FY6800(printsettings=True)
     |                          fy6800 = FY6XXX.FY6800("/dev/ttyUSB1",muteexceptions=True)
     |                          fy6800 = FY6XXX.FY6800("/dev/ttyUSB1", readtimeout=-0.80)
     |  
     |  aaddddSSyynnccMMooddee(self, syncobj)
     |      Add synchronization mode
     |      :param syncobj: string,  one of:
     |                      0 = Set Waveform of CH2 sync'ed with CH1
     |                      1 = Set Frequency of CH2 sync'ed with CH1
     |                      2 = Set Amplitude of CH2 sync'ed with CH1
     |                      3 = Set Offset of CH2 sync'ed with CH1
     |                      4 = Set Duty Cycle of CH2 sync'ed with CH1
     |      :return: 0xa
     |      NOTE: This function not available in sweep status
     |  
     |  ccaanncceellSSyynnccMMooddee(self, syncobj)
     |      Cancel synchronization mode
     |      :param syncobj: string,  one of:
     |                      0 = Cancel Waveform of CH2 sync'ed with CH1
     |                      1 = Cancel Frequency of CH2 sync'ed with CH1
     |                      2 = Cancel Amplitude of CH2 channel sync'ed with CH1
     |                      3 = Cancel Offset of CH2 sync'ed with CH1
     |                      4 = Cancel Duty Cycle of CH2 sync'ed with CH1
     |      :return: 0xa
     |  
     |  ggeettAASSKKmmooddee(self)
     |      Read ASK modulation mode
     |      :return:  integer, one of:
     |                0 = Normal output without trigger
     |                1 = Modulation mode of external signal input
     |                2 = Manual modulation.
     |  
     |  ggeettBBuuzzzzeerrSSttaattuuss(self)
     |      Read the buzzer on/off status
     |      :return: integer, 0 = disabled, 1 = enabled
     |  
     |  ggeettCChh11SSttaattuuss(self)
     |      Read the current enabled / disabled status of channel 1
     |      :return: integer,  0 = disabled, 1 = enabled
     |  
     |  ggeettCChh11WWaavvee(self)
     |      Read the current waveform for channel 1
     |      :return: integer index value for self.waveForms
     |  
     |  ggeettCChh11WWaavveeAAmmpplliittuuddee(self)
     |      Read the amplitude of the waveform set in channel 1
     |      :return: float, amplitude in volts
     |  
     |  ggeettCChh11WWaavveeDDeesscc(self)
     |      Read the  current waveform descriptor for channel 1
     |      :return: string, key from self.waveForms
     |  
     |  ggeettCChh11WWaavveeDDuuttyyCCyyccllee(self)
     |      Read channel 1 waveform duty cycle percentage
     |      :return: float representing duty cycle in percent
     |  
     |  ggeettCChh11WWaavveeFFrreeqq(self)
     |      Read the frequency of current waveform set in channel 1
     |      :return: string.  The frequency in Hz
     |  
     |  ggeettCChh11WWaavveeOOffffsseett(self)
     |      Read channel 1 waveform offset voltage
     |      :return: float, offset voltage in volts.
     |  
     |  ggeettCChh11WWaavveePPhhaassee(self)
     |      Read channel 1 waveform phase
     |      :return: float,  the phase in degrees
     |  
     |  ggeettCChh22SSttaattuuss(self)
     |      Read the current enabled / disabled status of channel 2
     |      :return: integer,  0 = disabled, 1 = enabled
     |  
     |  ggeettCChh22WWaavvee(self)
     |      Read the current waveform for channel 1
     |      :return: integer index value for self.waveForms
     |  
     |  ggeettCChh22WWaavveeAAmmpplliittuuddee(self)
     |      Read the amplitude of the waveform set in channel 2
     |      :return: float, amplitude in volts
     |  
     |  ggeettCChh22WWaavveeDDeesscc(self)
     |      Read the current waveform descriptor for channel 2
     |      :return: string, key from self.waveForms
     |  
     |  ggeettCChh22WWaavveeDDuuttyyCCyyccllee(self)
     |      Read channel 2 waveform duty cycle percentage
     |      :return: float representing duty cycle in percent
     |  
     |  ggeettCChh22WWaavveeFFrreeqq(self)
     |      Read the frequency of current waveform set in channel 2
     |      :return: string. The frequency in Hz
     |  
     |  ggeettCChh22WWaavveeOOffffsseett(self)
     |      Read channel 2 waveform offset voltage
     |      :return: float, offset voltage in volts.
     |  
     |  ggeettCChh22WWaavveePPhhaassee(self)
     |      Read channel 2 waveform phase
     |      :return: float,  the phase in degrees
     |  
     |  ggeettCCoouunntteerrCCnntt(self)
     |      Read frequency counter count value.
     |      :return: string, representing the count value.
     |  
     |  ggeettCCoouunntteerrCCnnttPPeerriioodd(self)
     |      Read frequency counter counting period.
     |      :return: string, representing counting period in ns
     |  
     |  ggeettCCoouunntteerrDDuuttyyCCyyccllee(self)
     |      Read frequency counter Duty Cycle.
     |      :return: string, representing duty cycle in percent
     |  
     |  ggeettCCoouunntteerrFFrreeqq(self)
     |      Read frequency counter frequency
     |      :return: string, representing the frequency in Hz
     |  
     |  ggeettCCoouunntteerrGGaatteeTTiimmee(self)
     |      Read frequency counter gate time.
     |      :return: integer, one of:
     |               0 =  1Sec
     |               1 =  10sec
     |               2 = 100sec
     |  
     |  ggeettCCoouunntteerrNNeeggPPuullsseeWWiiddtthh(self)
     |      Read frequency counter Negative Pulse Width
     |      :return: string, representing width of negative pulse in ns.
     |  
     |  ggeettCCoouunntteerrPPoossPPuullsseeWWiiddtthh(self)
     |      Read frequency counter Positive Pulse Width
     |      :return: string, representing width of positive pulse in ns.
     |  
     |  ggeettFFSSKKmmooddee(self)
     |      Read FSK modulation mode
     |      :return:  integer, one of:
     |                0 = Normal output without trigger
     |                1 = Modulation mode of external signal input
     |                2 = Manual modulation.
     |  
     |  ggeettFFSSKKsseeccoonnddaarryyFFrreeqq(self)
     |      Read FSK secondary frequency.
     |      :return: string, representing the FSK secondary frequency in Hz
     |  
     |  ggeettIIDD(self)
     |      Read serial number of the instrument
     |      :return: string, instrument serial number
     |  
     |  ggeettMMooddeell(self)
     |      Read model number of instrument
     |      :return: string, model number of instrument.
     |  
     |  ggeettPPSSKKmmooddee(self)
     |      Read PSK modulation mode
     |      :return:  integer, one of:
     |                0 = Normal output without trigger
     |                1 = Modulation mode of external signal input
     |                2 = Manual modulation.
     |  
     |  ggeettSSyynnccIInnffoo(self, syncobj)
     |      Read synchronization information
     |      :param syncobj: string, one of:
     |                       0 = Read Waveform sync info
     |                       1 = Read Frequency sync info
     |                       2 = Read Amplitude sync info
     |                       3 = Read Offset sync info
     |                       4 = Read Duty Cycle sync info
     |      :return:  integer, one of:
     |                        0   = disabled
     |                        255 = enabled
     |  
     |  ggeettTTrriiggggeerr(self)
     |      Read trigger mode of channel 1 waveform.
     |      :return:  integer,  one of:
     |                0 = No trigger
     |                1 = CH1 waveform triggered by CH2 waveform
     |                2 = CH1 waveform triggered by ExT.in connector
     |                3 = CH1 waveform triggered manually (one shot triggering)
     |  
     |  ggeettUUpplliinnkkMMooddee(self)
     |      Read uplink mode.
     |      :return:  integer:  0   = master
     |                          255 = slave .
     |  
     |  ggeettUUpplliinnkkSSttaattuuss(self)
     |      Read the uplink on/off status.
     |      :return: integer, 0 = off, 1 = on
     |  
     |  llooaaddPPaarraammss(self, position)
     |      Load system configuration
     |      :param position:  string, representing saved positions 01 - 20
     |      :return: 0xa
     |  
     |  ppaauusseeCCoouunntteerr(self, status)
     |      Pause frequency counter measurement.
     |      :param: status: string, one of:
     |                       0 = pause
     |                       1 = unpause
     |      :return: string, one of:
     |               current counter count if status = 0
     |               0x0a = unpaused if status = 1.
     |  
     |  rreeaaddPPuullsseeTTrriiggggeerr(self)
     |      Read pulse number of CH1 waveform
     |      :return: string respresenting the pulse number.
     |  
     |  rreesseettCCoouunntteerrCCnntt(self)
     |      Reset frequency counter count value.
     |      :return: x0a
     |  
     |  ssaavveePPaarraammss(self, position)
     |      Save system configuration into position
     |      :param position:  string respresnting position to save to 01 - 20
     |      :return: 0xa
     |  
     |  sseettAASSKKmmooddee(self, mode)
     |      Set ASK modulation mode of CH1 waveform
     |      :param mode: string, one of:
     |                   0 = Normal output without trigger
     |                   1 = Modulation mode of external signal input
     |                   2 = Manual modulation
     |      :return: x0a
     |  
     |  sseettBBuuzzzzeerrSSttaattuuss(self, status)
     |      Set buzzer on/off
     |      :param status: bool, 0 = off, 1 = on
     |      :return: x0a
     |  
     |  sseettCChh11SSttaattuuss(self, status)
     |      Set the channel 1 enabled / disabled status
     |      :param status: bool, 0 = disabled, 1 = enabled
     |      :return: 0xa
     |  
     |  sseettCChh11WWaavvee(self, waveindx)
     |      Set the active waveform for channel 1
     |      :param waveindx: integer.  Index to waveform  in self.waveForms
     |      :return: 0xa
     |  
     |  sseettCChh11WWaavveeAAmmpplliittuuddee(self, amplitude)
     |      Set the amplitude of the channel 1 waveform
     |      :param amplitude: string in the form  of x.xx
     |      :return:  0xa
     |  
     |  sseettCChh11WWaavveeBByyKKeeyy(self, key)
     |      Set the active waveform by key value
     |      :param key:string defined in self.Ch1WaveForms
     |      :return: 0xa
     |  
     |  sseettCChh11WWaavveeDDuuttyyCCyyccllee(self, dcycle)
     |      Set channel 1 waveform duty cycle percentage
     |      :param dcycle: string in form of x.xx percent
     |      :return: 0xa
     |  
     |  sseettCChh11WWaavveeFFrreeqq(self, freq)
     |      Set the waveform on channel 1
     |      :param freq: 14 character string in Hz
     |      :return: 0xa
     |  
     |  sseettCChh11WWaavveeOOffffsseett(self, offset)
     |      Set the channel 1 waveform offset voltage
     |      :param offset: string in the form of x.xx
     |      :return: 0xa
     |  
     |  sseettCChh11WWaavveePPhhaassee(self, phase)
     |      Set channel 1 waveform phase
     |      :param phase: string in form of x.xx degrees
     |      :return: 0xa
     |  
     |  sseettCChh11WWaavveePPuullsseePPeerriioodd(self, period)
     |      Set the pulse period of the channel 1 waveform
     |      :param period: string representing the period
     |      :return: 0xa
     |  
     |  sseettCChh22SSttaattuuss(self, status)
     |      Set the channel 2 enabled / disabled status
     |      :param status: bool, 0 = disabled, 1 = enabled
     |      :return: 0xa
     |  
     |  sseettCChh22WWaavvee(self, waveindx)
     |      Set the active waveform for channel 2
     |      :param waveindx: integer. Index to waveform in self.waveForms
     |      :return: 0xa
     |  
     |  sseettCChh22WWaavveeAAmmpplliittuuddee(self, amplitude)
     |      Set the amplitude of the channel 2 waveform
     |      :param amplitude: string in the form  of x.xx
     |      :return:  0xa
     |  
     |  sseettCChh22WWaavveeBByyKKeeyy(self, key)
     |      Set the channel 2 active waveform by key value
     |      :param key: string defined in self.Ch2WaveForms
     |      :return: 0xa
     |  
     |  sseettCChh22WWaavveeDDuuttyyCCyyccllee(self, dcycle)
     |      Set channel 2 waveform duty cycle percentage
     |      :param dcycle: string in form of x.xx percent
     |      :return: 0xa
     |  
     |  sseettCChh22WWaavveeFFrreeqq(self, freq)
     |      Set the waveform on channel 2
     |      :param freq: string, 14 characters in Hz
     |      :return: 0xa
     |  
     |  sseettCChh22WWaavveeOOffffsseett(self, offset)
     |      Set the channel 2 waveform offset voltage
     |      :param offset: string in the form of x.xx
     |      :return: 0xa
     |  
     |  sseettCChh22WWaavveePPhhaassee(self, phase)
     |      Set channel 2 waveform phase
     |      :param phase: string in form of x.xx degrees
     |      :return: 0xa
     |  
     |  sseettCCoouunntteerrCCoouupplliinnggMMooddee(self, mode)
     |      Set frequency counter coupling mode
     |      :param mode: string, one of:
     |                   0 = DC coupling
     |                   1 = AC coupling
     |      :return: x0a
     |  
     |  sseettCCoouunntteerrGGaatteeTTiimmee(self, time)
     |  
     |  sseettFFSSKKmmooddee(self, mode)
     |      Set FSK modulation mode of CH1 waveform
     |      :param mode: string, one of:
     |                   0 = Normal output without trigger
     |                   1 = Modulation mode of external signal input
     |                   2 = Manual modulation
     |      :return: x0a
     |  
     |  sseettFFSSKKsseeccoonnddaarryyFFrreeqq(self, freq)
     |      Set secondary frequency of CH1 waveform FSK
     |      :param freq: string, representing the FSK secondary frequency in Hz
     |      :return: 0xa
     |  
     |  sseettPPSSKKmmooddee(self, mode)
     |      Set PSK modulation mode of CH1 waveform
     |      :param mode: string, one of:
     |                   0 = Normal output without trigger
     |                   1 = Modulation mode of external signal input
     |                   2 = Manual modulation
     |      :return: x0a
     |  
     |  sseettPPuullsseeTTrriiggggeerr(self, pulseamt)
     |      Set pulse number of CH1 waveform when triggered. Limits how many cycles
     |      of the CH1 waveform will ouput.
     |      :param pulseamt: string representing pulse number from 1 to 1048575
     |      :return:
     |  
     |  sseettSSwweeeeppCCoonnttrroollSSoouurrccee(self, source)
     |      Set control source of sweep.
     |      :param source: string, one of:
     |                     0 = control source is time
     |                     1 = control source is analog signal input from VCO IN terminal
     |      :return: x0a
     |  
     |  sseettSSwweeeeppEEnnddPPooss(self, data)
     |      Set END position of sweep
     |      :param data: string, depends on setting of obj in setSweepObject()
     |                    if obj is: 0, data = frequency in Hz
     |                               1, data = amplitude in Volts
     |                               2, data = offset in Volts
     |                               3, data = duty cycle in %
     |      :return: x0a
     |  
     |  sseettSSwweeeeppMMooddee(self, mode)
     |      Set sweep mode.
     |      :param mode: string, one of:
     |                   0 = Linear sweep
     |                   1 = Log sweep
     |      :return: x0a
     |  
     |  sseettSSwweeeeppOObbjjeecctt(self, obj)
     |      Set object in sweep mode.
     |      :param obj: string, one of:
     |                  0 = set frequency to be object
     |                  1 = set amplitude to be object
     |                  2 = set offset to be object
     |                  3 = set duty cycle to be object
     |      :return:
     |  
     |  sseettSSwweeeeppSSttaarrttPPooss(self, data)
     |      Set START position of sweep
     |      :param data: string, depends on setting of obj in setSweepObject()
     |                    if obj is: 0, data = frequency in Hz
     |                               1, data = amplitude in Volts
     |                               2, data = offset in Volts
     |                               3, data = duty cycle in %
     |      :return: x0a
     |  
     |  sseettSSwweeeeppSSttaattuuss(self, status)
     |      Set sweep mode on/off
     |      :param status: bool, one of:
     |                     0 = sweep turned off
     |                     1 = sweep turned on
     |      :return: x0a
     |  
     |  sseettSSwweeeeppTTiimmee(self, time)
     |      Set sweep time.
     |      :param time: string, in form of xxx.xx
     |      :return: x0a
     |  
     |  sseettTTrriiggggeerr(self, triggersrc)
     |      Set trigger mode of channel 1 waveform.
     |      :triggersrc:   integer,  one of:
     |                      0 = Trigger disabled
     |                      1 = CH1 waveform triggered by CH2 waveform
     |                      2 = CH1 waveform triggered by ExT.in connector
     |                      3 = CH1 waveform triggered manually (one shot triggering)
     |                          The CH1 waveform is triggered each time command is sent.
     |      :return: x0a
     |  
     |  sseettUUpplliinnkkMMooddee(self, mode)
     |      Set uplink mode
     |      :param mode: string, 0 = master, 1 = slave
     |      :return: x0a
     |  
     |  sseettUUpplliinnkkSSttaattuuss(self, status)
     |      Set uplink on/off
     |      :param status:  bool, 0 = off, 1 = on
     |      :return: x0a
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  ____ddiicctt____
     |      dictionary for instance variables (if defined)
     |  
     |  ____wweeaakkrreeff____
     |      list of weak references to the object (if defined)
    
    class FFYY66XXXXXX__SSeerriiaall(__builtin__.object)
     |  Methods defined here:
     |  
     |  ____ddeell____(self)
     |  
     |  ____iinniitt____(self, device=None, muteexceptions=False, readtimeout=1, writetimeout=0.25)
     |      Create a serial port object based on the FY6xxx device
     |      :param device:         string. Valid serial port such as "/dev/ttyUSB1"
     |      :param muteexceptions: bool.  Mute serial port open / read / write exceptions.
     |  
     |  cclloossee(self)
     |      Closes the open serial port device
     |      :return: None
     |  
     |  fflluusshhiinnppuutt(self)
     |      flushes the serial input buffers
     |      :return: None
     |  
     |  rreeaadd(self, size)
     |      read size number of bytes from serial device
     |      :param size: integer
     |      :return:     the data read from serial device
     |  
     |  rreeaaddlliinnee(self)
     |      Read data from serial device until 1 of following occurs:
     |          1.  An 0xa (LF)is  detected in data stream
     |          2.  serial.timeout seconds has elapsed
     |      serial.timeout can be adjusted by specifying readtimeout=
     |      :return: The data read from serial device
     |  
     |  wwrriittee(self, cmd)
     |      Write data to the serial device
     |      :return: integer, if write timeout is configured for the port and the time is exceeded.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  ____ddiicctt____
     |      dictionary for instance variables (if defined)
     |  
     |  ____wweeaakkrreeff____
     |      list of weak references to the object (if defined)

DDAATTAA
    CChh11WWaavveeFFoorrmmss = {'AM': '31', 'Adj Pulse': '03', 'CMOS': '02', 'Chirp': ...
    CChh22WWaavveeFFoorrmmss = {'AM': '30', 'CMOS': '02', 'Chirp': '32', 'DC': '03', '...
    wwaavveeFFoorrmmss = ('Sine', 'Square', 'CMOS', 'Adj Pulse', 'DC', 'Triangle', ...

