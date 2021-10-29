from PIL import Image

mac = Image.open('mac-network-sharing.png')

print(type(mac))

print(mac.format_description)
print(mac.size)

target = mac.crop((0,0,200,200))

target.save("1.png")

output = mac.paste(im=target, box=(300,300))

mac.save("2.png")

output = mac.resize((3000,5000))
output.save("3.png")

mac.putalpha(30)
mac.save("4.png")

target.putalpha(128)

output = mac.paste(im=target, box=(300,300), mask=target)

mac.save("2.png")