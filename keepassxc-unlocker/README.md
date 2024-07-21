Auto-unlocker for [KeePassXC](https://github.com/keepassxreboot/keepassxc).

Takes passwords from system keyring using `libsecret` and unlocks kdbx databases by listening and sending D-Bus messages.

## Requirements
Check requirements [here](keepassxc-unlocker#L10).

## Installation
1. Add passwords for your kdbx databases to keyring:
```bash
keepassxc-unlocker add ~/database1.kdbx
keepassxc-unlocker add ~/database2.kdbx
```
2. Add keepassxc-unlocker to autostart
```bash
keepassxc-unlocker autostart add
```
3. Set up KeePassXC to automatically launch at system startup
