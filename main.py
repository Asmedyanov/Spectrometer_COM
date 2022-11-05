# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial

Ser_Port = serial.Serial()


def try_open_serial(ser: serial.Serial):
    ser.baudrate = 19200
    for i in range(20):
        ser.port = f"COM{i}"
        try:
            ser.open()
            print(f"COM{i} is opened")
            return
        except:
            print(f"NO COM{i}")


def send_com_messege(ser: serial.Serial):
    if not ser.isOpen():
        print("Port is not opened")
        return
    messege_list = [
        b'AE20',#set slit 20 mkm
        b'CG3.0',#set calibrate current grating 3.0 mkm
        b'DE20',#set default entrance slit width 20 mkm
        b'DG3',#set default grating 150 g/mm
        b'GW0.6',#go to wave langth 0.6 mkm
        b'GS3',#grating select 150 g/mm
        b'DA',#Default wavelength
        b'RE'#reset
    ]
    for comand in messege_list:
        try:
            ser.write(comand)
            print(f'{comand} is send')
        except:
            print(f'{comand} is not send')


try_open_serial(Ser_Port)
send_com_messege(Ser_Port)
try:
    Ser_Port.close()
except:
    print('Nothing to close')
