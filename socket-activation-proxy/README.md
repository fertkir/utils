On-demand tunnel creator based on systemd-sockets. 
Based on [this implementation](https://unix.stackexchange.com/questions/383678/on-demand-ssh-socks-proxy-through-systemd-user-units-with-socket-activation-does/635178#635178).

## Installation
1. Put `.socket-activation-proxy.json` file to your `$HOME`:
```json
[
  {
    "name": "ssh-socks",
    "port": 8070,
    "command": "/usr/bin/ssh -N -D %PORT% server"
  },
  {
    "name": "remote-router",
    "port": 8080,
    "command": "/usr/bin/ssh -N -L %PORT%:192.168.1.1:80 server"
  },
  {
    "name": "shadowsocks",
    "port": 8090,
    "command": "%h/.cargo/bin/sslocal -b 127.0.0.1:%PORT% -c %h/.shadowsocks.json"
  }
]
```
2. Run:
```bash
socket-activation-proxy
```

This will generate and enable required systemd user units.
