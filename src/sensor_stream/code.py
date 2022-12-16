from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_clue import clue

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

while True:
    ble.start_advertising(advertisement)
    print("Waiting to connect")
    while not ble.connected:
        pass
    print("Connected")
    while ble.connected:
        s = uart.readline()
        if s:
            uart.write(
                "xyzpth: {:.2f} {:.2f} {:.2f} {:.3f} {:.1f} {:.1f}\n".format(
                    clue.acceleration[0],
                    clue.acceleration[1],
                    clue.acceleration[2],
                    clue.pressure,
                    clue.temperature,
                    clue.humidity,
                ).encode("utf-8")
            )
