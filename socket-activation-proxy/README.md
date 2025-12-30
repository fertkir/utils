On-demand tunnel creator based on systemd-sockets. 
Based on [this implementation](https://unix.stackexchange.com/questions/383678/on-demand-ssh-socks-proxy-through-systemd-user-units-with-socket-activation-does/635178#635178).

## Installation
1. Put your config files to `$HOME/.config/socket-activation-proxy/`, e.g.
```bash
# $HOME/.config/socket-activation-proxy/ssh-socks.conf
PORT=8070
COMMAND="/usr/bin/ssh -N -D %PORT% server"

# $HOME/.config/socket-activation-proxy/remote-router.conf
PORT=8080
COMMAND="/usr/bin/ssh -N -L %PORT%:192.168.1.1:80 server"

# $HOME/.config/socket-activation-proxy/shadowsocks.conf
PORT=8090
COMMAND="%h/.cargo/bin/sslocal -b 127.0.0.1:%PORT% -c %h/.shadowsocks.json"
```
2. Run:
```bash
socket-activation-proxy
```

This will generate and enable required systemd user units.
