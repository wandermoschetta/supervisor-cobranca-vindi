from datetime import datetime
import time
import psutil
import os


process_name = "python.exe"
cmd_start_file = str(
    "start C:\\Users\\Administrator\\Desktop\\start-vindi-pagamentos.bat cmd.exe")


def check_on_process():
    is_up_vindi_process = False

    for proc in psutil.process_iter():
        if proc.name() == process_name:
            if str(proc.cmdline()[1]) == "main.py":
                is_up_vindi_process = True
                print("-> PROCESSO DA VINDI EM EXECUCAO - [ OK ] ")

    if not is_up_vindi_process:
        print("")
        print(" >> STARTANDO PROCESSO DA VINDI EM {} ".format(cmd_start_file))
        os.system(cmd_start_file)


def main():
    print('**** STARTANDO SUPERVISOR VINDI **** ')

    while True:
        data_agora = datetime.now()
        print(
            '---- INICIO SUPERVISOR {} ----'.format(data_agora.__str__()[:19]))
        print('')
        print('')
        check_on_process()
        time.sleep(60)
        print('')
        print('')


if __name__ == '__main__':
    main()
