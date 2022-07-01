# kasa-cli
 A command-line application (standalone executable) for TP-Link Kasa Smarthome products like smart WiFi switches and more.

 Note: there's really not much to this project except for build scripts:

 - The code is simply a wrapper around the awesome [python-kasa](https://github.com/python-kasa/python-kasa) library.
 - The executable is built with [nuitka](https://github.com/Nuitka/Nuitka), the amazing python compiler that's written in python.
 
# Example Usage
Turn Switch OFF  
`.\kasa_cli.exe --host 192.168.1.118 off`

Turn Switch ON  
`.\kasa_cli.exe --host 192.168.1.118 on`  

See [python-kasa > Command-line usage](https://python-kasa.readthedocs.io/en/latest/cli.html) for more full details.

`.\kasa_cli.exe --help`

```
Usage: kasa [OPTIONS] COMMAND [ARGS]...

  A tool for controlling TP-Link smart home devices.

Options:
  --host TEXT                     The host name or IP address of the device to
                                  connect to.
  --alias TEXT                    The device name, or alias, of the device to
                                  connect to.
  --target TEXT                   The broadcast address to be used for
                                  discovery.  [default: 255.255.255.255]
  -d, --debug
  --type [plug|bulb|dimmer|strip|lightstrip]
  --version                       Show the version and exit.
  --help                          Show this message and exit.

Commands:
  alias        Get or set the device (or plug) alias.
  brightness   Get or set brightness.
  discover     Discover devices in the network.
  effect       Set an effect.
  emeter       Query emeter for historical consumption.
  hsv          Get or set color in HSV.
  led          Get or set (Plug's) led state.
  off          Turn the device off.
  on           Turn the device on.
  raw-command  Run a raw command on the device.
  reboot       Reboot the device.
  schedule     Scheduling commands.
  state        Print out device state and versions.
  sysinfo      Print out full system information.
  temperature  Get or set color temperature.
  time         Get the device time.
  usage        Query usage for historical consumption.
  wifi         Commands to control wifi settings.
  ```
