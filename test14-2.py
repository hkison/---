for i in range(2,10):
    f = open(f"99dan/{i}단.txt","w")
    for j in range(1,10):
        f.write(f"{i}x{j} = {i*j}\n")