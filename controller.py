from __future__ import absolute_import
import threading
import time


from appframe.core_control import CoreControl
from honeywell.topeni import Topeni
from lsw3.InverterDataReg import DataReg

if __name__ == "__main__":
    dr = DataReg()
    dr_thread = threading.Thread(target=dr.run)

    topeni = Topeni()
    topeni_thread = threading.Thread(target=topeni.run)

    dr_thread.start()
    topeni_thread.start()

    while not CoreControl.stop_flag:
        time.sleep(1)
    dr_thread.join()
    topeni_thread.join()
    print("Konec")
