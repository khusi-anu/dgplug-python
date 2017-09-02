#!/usr/bin/env python3

def get_cpu_cores():
    with open("/proc/cpuinfo") as cpu_file:
        cpu_info = cpu_file.read()
        return cpu_info.count("processor")
if __name__ == '__main__':
    print("Number of virtual processors are: ", get_cpu_cores())
