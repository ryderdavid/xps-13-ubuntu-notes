# Enable Suspend to Hibernate

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

4. By default Ubuntu cannot time out to suspend-then-hibernate; creating a symlink in `/usr/lib/systemd/system` fixes this:

```
cd /usr/lib/systemd/system
sudo mv systemd-suspend.service systemd-suspend.service.old
sudo ln -s systemd-suspend-then-hibernate.service systemd-suspend.service
```
