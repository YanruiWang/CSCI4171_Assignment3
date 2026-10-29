def read_bridge_fdb():
    with open("BridgeFDB.txt", "r") as f:
        arr = dict()
        file_iter = iter(f)
        for line1, line2 in zip(file_iter, file_iter):
            addr = line1.replace("\n", "")
            port = int(line2)
            arr[addr] = port

        return arr

def read_random_frames():
    with open("RandomFrames.txt", "r") as f:
        arr = list()
        file_iter = iter(f)
        for line1, line2, line3 in zip(file_iter, file_iter, file_iter):
            source_addr = line1.replace("\n", "")
            dest_addr = line2.replace("\n", "")
            port = int(line3)
            arr.append((source_addr, dest_addr, port))
        return arr


data_fdb = read_bridge_fdb()

rand_frames = read_random_frames()

output = list()
for frame in rand_frames:
    source_addr = frame[0]
    dest_addr = frame[1]
    source_port = frame[2]
    if data_fdb.get(dest_addr) is None:
       output.append(f"{source_addr}    {dest_addr}    {source_port}     Broadcast")
    else:
        dest_port = data_fdb[dest_addr]
        if dest_port == source_port:
            output.append(f"{source_addr}    {dest_addr}    {source_port}    Discard")
        else:
            output.append(f"{source_addr}    {dest_addr}    {source_port}    Forwarded on port {dest_port}")
    data_fdb[source_addr] = source_port

with open("BridgeOutput.txt", "w") as f:
    f.write("\n".join(output)+"\n")


db_str_arr = list()
# print(data_fdb)
for addr, port in data_fdb.items():
    db_str_arr.append(f"{addr}\n{port}")

with open("BridgeFDB.txt", "w") as f:
    pass
    f.write("\n".join(db_str_arr)+"\n")