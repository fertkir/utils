## Requirements
[Required packages](keepassxc-unlocker/keepassxc-unlocker#L10)

## Installation
1. Add passwords for your kdbx databases to keyring:
```bash
keepass-unlocker add ~/database1.kdbx
keepass-unlocker add ~/database2.kdbx
```
2. Add keepassxc-unlocker to autostart
```bash
keepassxc-unlocker autostart add
```
3. Log out and log in back
