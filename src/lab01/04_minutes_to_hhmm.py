m=int(input("Минуты: "))
print(f"Минуты: {m}")
h=m//60
ze=(2-len(str(m%60)))*'0'
print(f"{h}:{ze}{m%60}")