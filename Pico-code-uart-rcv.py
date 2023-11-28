import machine
import time

# Set UART parameters for UART1 using GPIO 26 as TX and GPIO 27 as RX
uart = machine.UART(0, baudrate=9600, tx=16, rx=17)

while True:
    if uart.any():
        received_data = uart.read(uart.any())
        decoded_data = received_data.decode('utf-8')  # Decode bytes to string
        integer_data = int(decoded_data)
        print("Received data:", integer_data)
    
    time.sleep(0.1)  # Optional delay to reduce CPU usage
