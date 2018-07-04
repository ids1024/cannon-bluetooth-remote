This is a simple Python script to emulate the BR-E1 remote, for controlling Bluetooth enabled Canon DSLRs like the Rebel T7i. [This blog post](https://iandouglasscott.com/2018/07/04/canon-dslr-bluetooth-remote-protocol/).

This script does not provide a particularly good interface. It is meant as a demonstration of the protocol. Look at the code and adapt to your own use.

This script requires `btgatt-client` from `bluez-utils`. To pair with the Camera, you will need the camera's Bluetooth MAC address, which can be found under it's Bluetooth settings menu. Then enable Bluetooth on the camera, set the "Bluetooth function" to "Remote" and click pair. On your computer, run `./remote.py <address> pair`.

You can then execute commands. For example, `./remote.py <address> ir` releases the shutter immediately.
