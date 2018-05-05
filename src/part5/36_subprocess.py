# -*- coding: utf-8 -*-


'''
subprocess是当前最好的调用子进程的内置模块,
由python启动的子进程是可以平行运作的.
'''

import os
import time
import subprocess


# 获取子进程输出
proc = subprocess.Popen(
    ['echo', 'Hello from the child!'],
    stdout=subprocess.PIPE)
out, err = proc.communicate()

print(f"status: {err}, response: {out.decode('utf-8')}")

# 定期检查子进程的状态，一边处理其他事务。
proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
    print('Working ...')
    # some time-consuming work here
    # ...

print('Exit status', proc.poll())


# 子进程从父进程中剥离，平行运行子进程


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


start = time.time()
# 先启动所有的子进程
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

# 然后通过communicate方法，等待这些子进程完成其io工作并终结
for proc in procs:
    proc.communicate()
end = time.time()

print(f"Finished in {end - start:.3f} seconds")


# python程序与子进程的交互
def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Q13s\x11'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()   # ensure the child get input
    return proc


procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)

for proc in procs:
    out, err = proc.communicate()
    print(out)


# 实现类似shell中管道的功能
def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5'],
        stdin=input_stdin,
        stdout=subprocess.PIPE)
    return proc


input_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc)
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc)

# 必须先要执行这段
for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out, err = proc.communicate()
    print(out.strip())


# 限定子进程的时间, 超出终止子进程
proc = run_sleep(10)
try:
    proc.communicate(timeout=0.5)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('Exit status', proc.poll())
