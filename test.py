from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://github.com/seblambert/Pico1_OTA/blob/main"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test.py")

ota_updater.download_and_install_update_if_available()

print("version 2")
