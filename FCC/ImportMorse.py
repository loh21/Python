import morse

message = "SOS We have hit an iceberg and need help quickly"


morse_message = morse.encode(message)

print(f"Incoming message: {message}")
print(f"   Morse encoded: {morse_message}")


morse1 = "... . -.-. .-. . - / -- . ... ... .- --. ."

decode_message = morse.decode(morse1)

print(f"Incoming message: {morse1}")
print(f"   Morse decoded: {decode_message}")