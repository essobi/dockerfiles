FROM scratch  
  
ADD lime_2016-12-25.tar.xz /  
  
RUN chmod o+x /usr/lib/dbus-1.0/dbus-daemon-launch-helper  
  
RUN rc-status && rc-service dbus restart && pisi it
https://sourceforge.net/projects/limelinux/files/package/g/gawk/gawk-4.1.3-1-lm-x86_64.pisi
--ignore-check --ignore-dep --ignore-safety -dv  

