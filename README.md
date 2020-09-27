# Ubuntu Tweaks

## Enable Suspend to Hibernate

1. Disable secure boot in BIOS
2. `sudo nano /etc/systemd/sleep.conf`: 

```
[Sleep]
AllowSuspend=yes
AllowHibernation=yes
AllowSuspendThenHibernate=yes
AllowHybridSleep=yes
HibernateDelaySec=3600

```
3. `sudo nano /etc/systemd/logind.conf`:

```
[Sleep]
AllowSuspend=yes
AllowHibernation=yes
AllowSuspendThenHibernate=yes
AllowHybridSleep=yes
HibernateDelaySec=3600
```
