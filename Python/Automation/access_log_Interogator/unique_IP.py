# declare a set
ipset = set()

for line in open('access_log'):
    ip = line.split(' ')[0]
    ipset.add(ip)

for ip in ipset:
    print (ip)

print("-------------------------------------------------")
print("Total unique IP addresses:" + str(len(ipset)))