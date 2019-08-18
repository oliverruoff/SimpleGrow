# Raspi Simple Grow to keep your plants watered! 

## Setting things up for linux systems (developed for Raspberry Pi)

* Install python3
* Install modules listed in `requirements.txt`
* Copy `simplegrow.py` to raspberry pi
* Change the variables `TIMES_TO_WATER`, `PUMP_WATERING_TIME` and `PUMP_PIN` at the top of `simplegrow.py` script to your needs
* Make `simplegrow.py` executable
    * $ `chmod +x simplegrow.py`
* Copy `sg.service` to `/lib/systemd/system`
* Change `ExecStart=` command inside `sg.service` accordingly to path where `simplegrow.py` was copied
* Enable daemon process
    * $ `sudo systemctl daemon-reload`
    * $ `sudo systemctl enable sg.service`
    * $ `sudo systemctl start sg.service`

## Useful commands for process monitoring

* Check status
    * $ `sudo systemctl status sg.service`
* Start service
    * $ `sudo systemctl start sg.service`
* Stop service
    * $ `sudo systemctl stop sg.service`
* Check service's log
    * $ `sudo journalctl -f -u sg.service`