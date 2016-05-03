#!/usr/bin/python
s=open("/etc/hosts").read()
s=s.replace("localhost", "localhost kafka-1")
f=open("/etc/hosts", 'w')
f.write(s)
f.flush()
f.close()
