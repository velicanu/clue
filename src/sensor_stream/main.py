from datetime import datetime

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

ble = BLERadio()

uart_connection = None


file_ = open("dump.txt", "w")
try:
    while True:
        if not uart_connection:
            print("Trying to connect...")
            for adv in ble.start_scan(ProvideServicesAdvertisement):
                if UARTService in adv.services:
                    uart_connection = ble.connect(adv)
                    print("Connected")
                    break
            ble.stop_scan()

        if uart_connection and uart_connection.connected:
            uart_service = uart_connection[UARTService]
            while uart_connection.connected:
                uart_service.write("next\n".encode("utf-8"))
                line = uart_service.readline().decode("utf-8")
                if line:
                    line_ = f"{line.strip()} {datetime.now().timestamp()}\n"
                    file_.write(line_)
                    file_.flush()
                    print(line_.strip())
except KeyboardInterrupt:
    file_.close()
