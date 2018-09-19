print("Hello")
MF = 0.03125
s1 = input("Enter CAN message1 to be decoded MSB->LSB ")
type(s1)
convertedValue1 = int(s1, 16)
decoded_value1 = convertedValue1 * 0.03125
print("Decoded value for CAN message 1 is",decoded_value1)

s2 = input("Enter CAN message2 to be decoded MSB->LSB ")
type(s2)
convertedValue2 = int(s2, 16)
decoded_value2 = convertedValue2 * 0.03125
print("Decoded value for CAN message 2 is",decoded_value2)

s3 = input("Enter CAN message3 to be decoded MSB->LSB ")
type(s3)
convertedValue3 = int(s1, 16)
decoded_value3 = convertedValue3 * 0.03125
print("Decoded value for CAN message 3 is",decoded_value3)

s4 = input("Enter CAN message4 to be decoded MSB->LSB ")
type(s4)
convertedValue4 = int(s4, 16)
decoded_value4 = convertedValue4 * 0.03125
print("Decoded value for CAN message 4 is",decoded_value4)
