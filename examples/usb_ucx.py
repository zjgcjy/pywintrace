import time
import etw
def handle_usb_ucx(x):
    event = x[1]
    header = event['EventHeader']
    desc = header['EventDescriptor']
    if desc['Id'] in (26, 27):
        print(desc)

# https://winevt-kb.readthedocs.io/en/latest/sources/eventlog-providers/Provider-Microsoft-Windows-USB-UCX.html
def scan_etw():
    providers = [etw.ProviderInfo('Microsoft-Windows-USB-UCX', etw.GUID("{36da592d-e43a-4e28-af6f-4bc57c5a11e8}"))]
    job = etw.ETW(providers=providers, event_callback=handle_usb_ucx)
    job.start()
    time.sleep(20)
    job.stop()
scan_etw()
