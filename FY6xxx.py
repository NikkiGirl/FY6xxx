"""
Module: FY6xxx  FeelElec FY6800 serial communication protocol library
Version: 0.1
Date: 17Feb2019
Author: Nikki Cooper

For documentation issue the following on the command line:
pydoc FY6xxx

Licensed under the GPL v3 by Nikki Cooper.
"""

import serial


"""
Any differences between the FY6800 and the FY6600 are likely to be in one or all
of the following arrays. Everything else should be transparent.
"""
waveForms = ("Sine", "Square", "CMOS", "Adj Pulse", "DC", "Triangle",
             "Ramp", "Negative Ramp", "Stair Triangle", "Stairstep",
             "Negative Stairstep", "Positive Exponent", "Negative Exponent",
             "Positive Falling Exponent", "Negative Falling Exponent",
             "Positive Logrithm", "Negative Logrithm", "Positive Falling Logrithm",
             "Negative Falling Logrithm", "Positive Full Wave", "Negative Full Wave",
             "Positive Half Wave", "Negative Half Wave", "Lorentz Pulse", "Multitone",
             "Random Noise", "ECG", "Trapezoidal Pulse", "Sinc Pulse", "Impulse",
             "Gauss White Noise", "AM", "FM", "Chirp")

Ch1WaveForms = {'Sine': '00', 'Square': '01', 'CMOS': '02', 'Adj Pulse': '03', 'DC': '04', 'Triangle': '05',
                'Ramp': '06', 'Negative Ramp': '07', 'Stair Triangle': '08', 'Stairstep': '09',
                'Negative Stairstep': '10', 'Positive Exponent': '11', 'Negative Exponent': '12',
                'Positive Falling Exponent': '13', 'Negative Falling Exponent': '14',
                'Positive Logrithm': '15', 'Negative Logrithm': '16', 'Positive Falling Logrithm': '17',
                'Negative Falling Logrithm': '18', 'Positive Full Wave': '19', 'Negative Full Wave': '20',
                'Positive Half Wave': '21', 'Negative Half Wave': '22', 'Lorentz Pulse': '23',
                'Multitone': '24', 'Random Noise': '25', 'ECG': '26', 'Trapezoidal Pulse': '27',
                'Sinc Pulse': '28', 'Impulse': '29', 'Gauss White Noise': '30', 'AM': '31',
                'FM': '32', 'Chirp': '33'}

Ch2WaveForms = {'Sine': '00', 'Square': '01', 'CMOS': '02', 'DC': '03', 'Triangle': '04',
                'Ramp': '05', 'Negative Ramp': '06', 'Stair Triangle': '07', 'Stairstep': '08',
                'Negative Stairstep': '09', 'Positive Exponent': '10', 'Negative Exponent': '11',
                'Positive Falling Exponent': '12', 'Negative Falling Exponent': '13',
                'Positive Logrithm': '14', 'Negative Logrithm': '15', 'Positive Falling Logrithm': '16',
                'Negative Falling Logrithm': '17', 'Positive Full Wave': '18', 'Negative Full Wave': '19',
                'Positive Half Wave': '20', 'Negative Half Wave': '21', 'Lorentz Pulse': '22',
                'Multitone': '23', 'Random Noise': '24', 'ECG': '25', 'Trapezoidal Pulse': '26',
                'Sinc Pulse': '27', 'Impulse': '28', 'Gauss White Noise': '29', 'AM': '30',
                'FM': '31', 'Chirp': '32'}


class FY6XXX_Serial(object):
    def __init__(self, device=None, muteexceptions=False, readtimeout=1, writetimeout=0.25):
        """
        Create a serial port object based on the FY6xxx device
        :param device:         string. Valid serial port such as "/dev/ttyUSB1"
        :param muteexceptions: bool.  Mute serial port open / read / write exceptions.
        """
        self.device = device
        self.muteexceptions = muteexceptions

        self.port = serial.Serial(port=None, baudrate=115200,
                                  bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE, rtscts=False, dsrdtr=False,
                                  xonxoff=False, timeout=readtimeout, write_timeout=writetimeout)
        self.response = ''
        self.LF = "\n"
        self.cmd = ''

        try:
            self.port.port = self.device
            if self.device is not None:
                self.port.open()

        except (Exception, e):
            if not self.muteexceptions:
                print(str(e))
            exit(255)

        if self.port.isOpen():
            try:
                self.port.reset_input_buffer()
                self.port.reset_output_buffer()

            except (Exception, e):
                if not self.muteexceptions:
                    print("Error communicating... " + str(e))
                self.port.close()
                exit(254)
        return

    def __del__(self):
        if self.port.isOpen():
            self.port.close()

    def read(self, size):
        """
        read size number of bytes from serial device
        :param size: integer
        :return:     the data read from serial device
        """
        self.response = self.port.read(size)
        return self.response

    def readline(self):
        """
        Read data from serial device until 1 of following occurs:
            1.  An 0xa (LF)is  detected in data stream
            2.  serial.timeout seconds has elapsed
        serial.timeout can be adjusted by specifying readtimeout=
        :return: The data read from serial device
        """
        self.port.reset_input_buffer()
#       self.port.flush()
        self.response = self.port.read_until(size=20)
        return self.response

    def write(self, cmd):
        """
        Write data to the serial device
        :return: integer, if write timeout is configured for the port and the time is exceeded.
        """
        self.cmd = cmd + self.LF
        self.port.reset_input_buffer()
        self.port.write(self.cmd.encode())
        self.port.flush()
        return

    def close(self):
        """
        Closes the open serial port device
        :return: None
        """
        if self.port.isOpen():
            self.port.close()
        return

    def flushinput(self):
        """
        flushes the serial input buffers
        :return: None
        """
        self.port.reset_input_buffer()
        return


class FY6800(object):
    def __init__(self, device=None, printsettings=None, muteexceptions=False, readtimeout=1, writetimeout=0.25):
        """
        Setup serial port the FY6800 is connected as and contains all the
        necessary methods in order to read / write information to the FY6800

        :param device:         string, Serial port device such as /dev/ttyUSB1
        :param printsettings:  bool,   Print serial port parameters and exit program
        :param muteexceptions: bool,   Mute printing of serial port exception errors to console
        :param readtimeout:    float,  Set the read data from serial device timeout in sec. def: 1 sec
        :param writetimeout:   float,  Set the write data to serial device timeout in sec.  def: 0.25 sec

        :return   0:  Normal exit code
        :return 255:  Error opening serial device
        :return 254:  Error while reading or writing to / from serial device
        :return 253:  Serial port device was not specified. Default: None
        :return 252:  printsettings=True return code

        Example invocation: fy6800 = FY6xxx.FY6800("/dev/ttyUSB1")
                            fy6800 = FY6XXX.FY6800(printsettings=True)
                            fy6800 = FY6XXX.FY6800("/dev/ttyUSB1",muteexceptions=True)
                            fy6800 = FY6XXX.FY6800("/dev/ttyUSB1", readtimeout=-0.80)
        """
        self.printSettings = printsettings
        self.LF = "\n"
        self.settings = {'port': device, 'baudrate': 115200, 'bytesize': 8, 'parity': 'N', 'stopbits': 1,
                         'xonxoff': False, 'rtscts': False, 'dsrdtr': False, 'timeout': readtimeout,
                         'write_timeout': writetimeout, 'inter_byte_timeout': None}

        if self.printSettings is not None:
            for key, value in self.settings.items():
                print(key, value)
            exit(252)

        if device is None:
            print("device was specified as None.  Use a valid serial port such as /dev/ttyUSB1")
            exit(253)

        self.fy6800 = FY6XXX_Serial(device, muteexceptions, readtimeout, writetimeout)

        self.arbitrary = 0
        self.cmd = ''
        self.res = 0.0
        self.freq = ''
        self.response = ''
        self.waveIndx = 0
        self.waveForms = waveForms
        self.Ch1WaveForms = Ch1WaveForms
        self.Ch2WaveForms = Ch2WaveForms

        return

    # Ch 1 waveforms #

    def getCh1Wave(self):
        """
        Read the current waveform for channel 1
        :return: integer index value for self.waveForms
        """
        self.cmd = "RMW"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    def getCh1WaveDesc(self):
        """
        Read the  current waveform descriptor for channel 1
        :return: string, key from self.waveForms
        """
        self.cmd = "RMW"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        if self.response > 33:
            self.arbitrary = self.response - 33
            if self.arbitrary < 10:
                self.response = "Arbitrary 0" + str(self.arbitrary)
            else:
                self.response = "Arbitrary " + str(self.arbitrary)
            return self.response
        else:
            return self.waveForms[self.response]

    def setCh1Wave(self, waveindx):
        """
        Set the active waveform for channel 1
        :param waveindx: integer.  Index to waveform  in self.waveForms
        :return: 0xa
        """
        if waveindx < 10:
            self.waveIndx = "0" + str(waveindx)
        else:
            self.waveIndx = str(waveindx)
        self.cmd = "WMW" + self.waveIndx
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def setCh1WaveByKey(self, key):
        """
        Set the active waveform by key value
        :param key:string defined in self.Ch1WaveForms
        :return: 0xa
        """
        self.waveIndx = self.Ch1WaveForms[key]
        self.cmd = "WMW" + self.waveIndx
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh1WaveFreq(self):
        """
        Read the frequency of current waveform set in channel 1
        :return: string.  The frequency in Hz
        """
        self.cmd = "RMF"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def setCh1WaveFreq(self, freq):
        """
        Set the waveform on channel 1
        :param freq: 14 character string in Hz
        :return: 0xa
        """
        self.freq = freq
        self.cmd = "WMF" + self.freq
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh1WaveAmplitude(self):
        """
        Read the amplitude of the waveform set in channel 1
        :return: float, amplitude in volts
        """
        self.cmd = "RMA"
        self.fy6800.write(self.cmd)
        self.response = (float(self.fy6800.readline()) / 10000.0)
        return self.response

    def setCh1WaveAmplitude(self, amplitude):
        """
        Set the amplitude of the channel 1 waveform
        :param amplitude: string in the form  of x.xx
        :return:  0xa
        """
        self.cmd = "WMA" + amplitude
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh1WaveOffset(self):
        """
        Read channel 1 waveform offset voltage
        :return: float, offset voltage in volts.
        """
        self.cmd = "RMO"
        self.fy6800.write(self.cmd)
        self.response = float(self.fy6800.readline())
        self.res = (self.response - 4294967296) / 1000.0
        return self.res

    def setCh1WaveOffset(self, offset):
        """
        Set the channel 1 waveform offset voltage
        :param offset: string in the form of x.xx
        :return: 0xa
        """
        self.cmd = "WMO" + offset
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh1WavePhase(self):
        """
        Read channel 1 waveform phase
        :return: float,  the phase in degrees
        """
        self.cmd = "RMP"
        self.fy6800.write(self.cmd)
        self.response = float(self.fy6800.readline()) / 1000.0
        return self.response

    def setCh1WavePhase(self, phase):
        """
        Set channel 1 waveform phase
        :param phase: string in form of x.xx degrees
        :return: 0xa
        """
        self.cmd = "WMP" + phase
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh1WaveDutyCycle(self):
        """
        Read channel 1 waveform duty cycle percentage
        :return: float representing duty cycle in percent
        """
        self.cmd = "RMD"
        self.fy6800.write(self.cmd)
        self.response = float(self.fy6800.readline()) / 1000.0
        return self.response

    def setCh1WaveDutyCycle(self, dcycle):
        """
        Set channel 1 waveform duty cycle percentage
        :param dcycle: string in form of x.xx percent
        :return: 0xa
        """
        self.cmd = "WMD" + dcycle
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh1Status(self):
        """
        Read the current enabled / disabled status of channel 1
        :return: integer,  0 = disabled, 1 = enabled
        """
        self.cmd = "RMN"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    def setCh1Status(self, status):
        """
        Set the channel 1 enabled / disabled status
        :param status: bool, 0 = disabled, 1 = enabled
        :return: 0xa
        """
        self.cmd = "WMN" + str(status)
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def setCh1WavePulsePeriod(self, period):
        """
        Set the pulse period of the channel 1 waveform
        :param period: string representing the period
        :return: 0xa
        """
        self.cmd = "WMS" + period
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    # Ch2 waveforms #

    def getCh2Wave(self):
        """
        Read the current waveform for channel 1
        :return: integer index value for self.waveForms
        """
        self.cmd = "RFW"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    """
       NOTE:  There are some differences between the Ch1 wave table 
              and the Ch2 wave tables.  For waves >= 3, the offset is
              off by one, thus 1 is added to the index to get the values
              to match.   Therefore values returned by getCh1Wave() and getCh2Wave()
              are NOT the same.  This is a bug in the firmware.
              getCh1WaveDesc and getCh2WaveDesc account for this.
    """

    def getCh2WaveDesc(self):
        """
        Read the current waveform descriptor for channel 2
        :return: string, key from self.waveForms
        """
        self.cmd = "RFW"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())

        if self.response >= 3:
            self.response += 1

        if self.response > 33:
            self.arbitrary = self.response - 33
            if self.arbitrary < 10:
                self.response = "Arbitrary 0" + str(self.arbitrary)
            else:
                self.response = "Arbitrary " + str(self.arbitrary)
            return self.response
        else:
            return self.waveForms[self.response]

    def setCh2Wave(self, waveindx):
        """
        Set the active waveform for channel 2
        :param waveindx: integer. Index to waveform in self.waveForms
        :return: 0xa
        """
        if waveindx < 10:
            self.waveIndx = "0" + str(waveindx)
        else:
            self.waveIndx = str(waveindx)
        self.cmd = "WFW" + self.waveIndx
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def setCh2WaveByKey(self, key):
        """
        Set the channel 2 active waveform by key value
        :param key: string defined in self.Ch2WaveForms
        :return: 0xa
        """
        self.waveIndx = self.Ch2WaveForms[key]
        self.cmd = "WFW" + self.waveIndx
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh2WaveFreq(self):
        """
        Read the frequency of current waveform set in channel 2
        :return: string. The frequency in Hz
        """
        self.cmd = "RFF"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def setCh2WaveFreq(self, freq):
        """
        Set the waveform on channel 2
        :param freq: string, 14 characters in Hz
        :return: 0xa
        """
        self.cmd = "WFF" + freq
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh2WaveAmplitude(self):
        """
        Read the amplitude of the waveform set in channel 2
        :return: float, amplitude in volts
        """
        self.cmd = "RFA"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.read(6)
        self.amplitude = float(self.response) / 10000.0
        return self.amplitude

    def setCh2WaveAmplitude(self, amplitude):
        """
        Set the amplitude of the channel 2 waveform
        :param amplitude: string in the form  of x.xx
        :return:  0xa
        """
        self.cmd = "WFA" + amplitude
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh2WaveOffset(self):
        """
        Read channel 2 waveform offset voltage
        :return: float, offset voltage in volts.
        """
        self.cmd = "RFO"
        self.fy6800.write(self.cmd)
        self.response = float(self.fy6800.readline())
        self.res = (self.response - 4294967296) / 1000.0
        return self.res

    def setCh2WaveOffset(self, offset):
        """
        Set the channel 2 waveform offset voltage
        :param offset: string in the form of x.xx
        :return: 0xa
        """
        self.cmd = "WFO" + offset
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh2WavePhase(self):
        """
        Read channel 2 waveform phase
        :return: float,  the phase in degrees
        """
        self.cmd = "RFP"
        self.fy6800.write(self.cmd)
        self.response = float(self.fy6800.readline()) / 1000.0
        return self.response

    def setCh2WavePhase(self, phase):
        """
        Set channel 2 waveform phase
        :param phase: string in form of x.xx degrees
        :return: 0xa
        """
        self.cmd = "WFP" + phase
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh2WaveDutyCycle(self):
        """
        Read channel 2 waveform duty cycle percentage
        :return: float representing duty cycle in percent
        """
        self.cmd = "RFD"
        self.fy6800.write(self.cmd)
        self.response = float(self.fy6800.readline()) / 1000.0
        return self.response

    def setCh2WaveDutyCycle(self, dcycle):
        """
        Set channel 2 waveform duty cycle percentage
        :param dcycle: string in form of x.xx percent
        :return: 0xa
        """
        self.cmd = "WFD" + dcycle
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCh2Status(self):
        """
        Read the current enabled / disabled status of channel 2
        :return: integer,  0 = disabled, 1 = enabled
        """
        self.cmd = "RFN"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    def setCh2Status(self, status):
        """
        Set the channel 2 enabled / disabled status
        :param status: bool, 0 = disabled, 1 = enabled
        :return: 0xa
        """
        self.cmd = "WFN" + str(status)
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    #  System Settings commands #

    def loadParams(self, position):
        """
        Load system configuration
        :param position:  string, representing saved positions 01 - 20
        :return: 0xa
        """
        self.cmd = "ULN" + position
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def saveParams(self, position):
        """
        Save system configuration into position
        :param position:  string respresnting position to save to 01 - 20
        :return: 0xa
        """
        self.cmd = "USN" + position
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def addSyncMode(self, syncobj):
        """
        Add synchronization mode
        :param syncobj: string,  one of:
                        0 = Set Waveform of CH2 sync'ed with CH1
                        1 = Set Frequency of CH2 sync'ed with CH1
                        2 = Set Amplitude of CH2 sync'ed with CH1
                        3 = Set Offset of CH2 sync'ed with CH1
                        4 = Set Duty Cycle of CH2 sync'ed with CH1
        :return: 0xa
        NOTE: This function not available in sweep status
        """
        self.cmd = "USA" + syncobj
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def cancelSyncMode(self, syncobj):
        """
         Cancel synchronization mode
         :param syncobj: string,  one of:
                         0 = Cancel Waveform of CH2 sync'ed with CH1
                         1 = Cancel Frequency of CH2 sync'ed with CH1
                         2 = Cancel Amplitude of CH2 channel sync'ed with CH1
                         3 = Cancel Offset of CH2 sync'ed with CH1
                         4 = Cancel Duty Cycle of CH2 sync'ed with CH1
         :return: 0xa
         """
        self.cmd = "USD" + syncobj
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getSyncInfo(self, syncobj):
        """
        Read synchronization information
        :param syncobj: string, one of:
                         0 = Read Waveform sync info
                         1 = Read Frequency sync info
                         2 = Read Amplitude sync info
                         3 = Read Offset sync info
                         4 = Read Duty Cycle sync info
        :return:  integer, one of:
                          0   = disabled
                          255 = enabled
        """
        self.cmd = "RSA" + syncobj
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    def getBuzzerStatus(self):
        """
        Read the buzzer on/off status
        :return: integer, 0 = disabled, 1 = enabled
        """
        self.cmd = "RBZ"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        if self.response == 255:
            self.response = 1
        return self.response

    def setBuzzerStatus(self, status):
        """
        Set buzzer on/off
        :param status: bool, 0 = off, 1 = on
        :return: x0a
        """
        self.cmd = "UBZ" + str(status)
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getUplinkMode(self):
        """
        Read uplink mode.
        :return:  integer:  0   = master
                            255 = slave .
        """
        self.cmd = "RMS"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    def setUplinkMode(self, mode):
        """
        Set uplink mode
        :param mode: string, 0 = master, 1 = slave
        :return: x0a
        """
        self.cmd = "UMS" + mode
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getUplinkStatus(self):
        """
        Read the uplink on/off status.
        :return: integer, 0 = off, 1 = on
        """
        self.cmd = "RUL"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        if self.response == 255:
            self.response = 1
        return self.response

    def setUplinkStatus(self, status):
        """
        Set uplink on/off
        :param status:  bool, 0 = off, 1 = on
        :return: x0a
        """
        self.cmd = "UUL" + str(status)
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getID(self):
        """
        Read serial number of the instrument
        :return: string, instrument serial number
        """
        self.cmd = "UID"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def getModel(self):
        """
        Read model number of instrument
        :return: string, model number of instrument.
        """
        self.cmd = "UMO"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    # Modulation commands #

    def getTrigger(self):
        """
        Read trigger mode of channel 1 waveform.
        :return:  integer,  one of:
                  0 = No trigger
                  1 = CH1 waveform triggered by CH2 waveform
                  2 = CH1 waveform triggered by ExT.in connector
                  3 = CH1 waveform triggered manually (one shot triggering)
        """
        self.cmd = "RPM"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    def setTrigger(self, triggersrc):
        """
        Set trigger mode of channel 1 waveform.
        :triggersrc:   integer,  one of:
                        0 = Trigger disabled
                        1 = CH1 waveform triggered by CH2 waveform
                        2 = CH1 waveform triggered by ExT.in connector
                        3 = CH1 waveform triggered manually (one shot triggering)
                            The CH1 waveform is triggered each time command is sent.
        :return: x0a
         """
        self.cmd = "WPM" + triggersrc
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def readPulseTrigger(self):
        """
        Read pulse number of CH1 waveform
        :return: string respresenting the pulse number.
        """
        self.cmd = "RPN"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def setPulseTrigger(self, pulseamt):
        """
        Set pulse number of CH1 waveform when triggered. Limits how many cycles
        of the CH1 waveform will ouput.
        :param pulseamt: string representing pulse number from 1 to 1048575
        :return:
        """
        self.cmd = "WPN" + pulseamt
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getASKmode(self):
        """
        Read ASK modulation mode
        :return:  integer, one of:
                  0 = Normal output without trigger
                  1 = Modulation mode of external signal input
                  2 = Manual modulation.
        """
        self.cmd = "RTA"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    def setASKmode(self, mode):
        """
        Set ASK modulation mode of CH1 waveform
        :param mode: string, one of:
                     0 = Normal output without trigger
                     1 = Modulation mode of external signal input
                     2 = Manual modulation
        :return: x0a
        """
        self.cmd = "WTA" + mode
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getFSKmode(self):
        """
        Read FSK modulation mode
        :return:  integer, one of:
                  0 = Normal output without trigger
                  1 = Modulation mode of external signal input
                  2 = Manual modulation.
        """
        self.cmd = "RTF"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    def setFSKmode(self, mode):
        """
        Set FSK modulation mode of CH1 waveform
        :param mode: string, one of:
                     0 = Normal output without trigger
                     1 = Modulation mode of external signal input
                     2 = Manual modulation
        :return: x0a
        """
        self.cmd = "WTF" + mode
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getFSKsecondaryFreq(self):
        """
        Read FSK secondary frequency.
        :return: string, representing the FSK secondary frequency in Hz
        """
        self.cmd = "RFK"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def setFSKsecondaryFreq(self, freq):
        """
        Set secondary frequency of CH1 waveform FSK
        :param freq: string, representing the FSK secondary frequency in Hz
        :return: 0xa
        """
        self.cmd = "WFK" + freq
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getPSKmode(self):
        """
        Read PSK modulation mode
        :return:  integer, one of:
                  0 = Normal output without trigger
                  1 = Modulation mode of external signal input
                  2 = Manual modulation.
        """
        self.cmd = "RTP"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.readline())
        return self.response

    def setPSKmode(self, mode):
        """
        Set PSK modulation mode of CH1 waveform
        :param mode: string, one of:
                     0 = Normal output without trigger
                     1 = Modulation mode of external signal input
                     2 = Manual modulation
        :return: x0a
        """
        self.cmd = "WTP" + mode
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    # Frequency counter measurement commands #

    def setCounterCouplingMode(self, mode):
        """
        Set frequency counter coupling mode
        :param mode: string, one of:
                     0 = DC coupling
                     1 = AC coupling
        :return: x0a
        """
        self.cmd = "WCC" + mode
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def getCounterFreq(self):
        """
        Read frequency counter frequency
        :return: string, representing the frequency in Hz
        """
        self.cmd = "RCF"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def getCounterCnt(self):
        """
        Read frequency counter count value.
        :return: string, representing the count value.
        """
        self.cmd = "RCC"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def resetCounterCnt(self):
        """
        Reset frequency counter count value.
        :return: x0a
        """
        self.cmd = "WCZ0"
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def pauseCounter(self, status):
        """
        Pause frequency counter measurement.
        :param: status: string, one of:
                         0 = pause
                         1 = unpause
        :return: string, one of:
                 current counter count if status = 0
                 0x0a = unpaused if status = 1.
        """
        self.cmd = "WCP" + status
        self.fy6800.write(self.cmd)
        if status == "0":
            response = self.fy6800.readline()
            return response.strip(self.LF)
        else:
            self.fy6800.flushinput()
            return hex(ord(self.fy6800.read(1)))

    def getCounterCntPeriod(self):
        """
        Read frequency counter counting period.
        :return: string, representing counting period in ns
        """
        self.cmd = "RCT"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def getCounterPosPulseWidth(self):
        """
        Read frequency counter Positive Pulse Width
        :return: string, representing width of positive pulse in ns.
        """
        self.cmd = "RC+"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def getCounterNegPulseWidth(self):
        """
         Read frequency counter Negative Pulse Width
         :return: string, representing width of negative pulse in ns.
         """
        self.cmd = "RC-"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def getCounterDutyCycle(self):
        """
        Read frequency counter Duty Cycle.
        :return: string, representing duty cycle in percent
        """
        self.cmd = "RCD"
        self.fy6800.write(self.cmd)
        self.response = self.fy6800.readline()
        return self.response.decode().strip(self.LF)

    def getCounterGateTime(self):
        """
        Read frequency counter gate time.
        :return: integer, one of:
                 0 =  1Sec
                 1 =  10sec
                 2 = 100sec
        """
        self.cmd = "RCG"
        self.fy6800.write(self.cmd)
        self.response = int(self.fy6800.read(1))
        return self.response

    def setCounterGateTime(self, time):
        self.cmd = "WCG" + time
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    # Sweep commands #

    def setSweepObject(self, obj):
        """
        Set object in sweep mode.
        :param obj: string, one of:
                    0 = set frequency to be object
                    1 = set amplitude to be object
                    2 = set offset to be object
                    3 = set duty cycle to be object
        :return:
        """
        self.cmd = "SOB" + obj
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def setSweepStartPos(self, data):
        """
        Set START position of sweep
        :param data: string, depends on setting of obj in setSweepObject()
                      if obj is: 0, data = frequency in Hz
                                 1, data = amplitude in Volts
                                 2, data = offset in Volts
                                 3, data = duty cycle in %
        :return: x0a
        """
        self.cmd = "SST" + data
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def setSweepEndPos(self, data):
        """
        Set END position of sweep
        :param data: string, depends on setting of obj in setSweepObject()
                      if obj is: 0, data = frequency in Hz
                                 1, data = amplitude in Volts
                                 2, data = offset in Volts
                                 3, data = duty cycle in %
        :return: x0a
        """
        self.cmd = "SEN" + data
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def setSweepTime(self, time):
        """
        Set sweep time.
        :param time: string, in form of xxx.xx
        :return: x0a
        """
        self.cmd = "STI" + time
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def setSweepMode(self, mode):
        """
        Set sweep mode.
        :param mode: string, one of:
                     0 = Linear sweep
                     1 = Log sweep
        :return: x0a
        """
        self.cmd = "SMO" + mode
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    def setSweepStatus(self, status):
        """
        Set sweep mode on/off
        :param status: bool, one of:
                       0 = sweep turned off
                       1 = sweep turned on
        :return: x0a
        """
        self.cmd = "SBE" + str(status)
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))

    #   source: 0 = time
    #           1 = Vco IN
    def setSweepControlSource(self, source):
        """
        Set control source of sweep.
        :param source: string, one of:
                       0 = control source is time
                       1 = control source is analog signal input from VCO IN terminal
        :return: x0a
        """
        self.cmd = "SXY" + source
        self.fy6800.write(self.cmd)
        return hex(ord(self.fy6800.read(1)))
