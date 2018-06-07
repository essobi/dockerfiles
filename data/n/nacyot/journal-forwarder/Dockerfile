FROM fedora/systemd-systemd  
RUN yum install -y nc  
# -v /var/log/journal:/var/log/journal:ro  
# -v /etc/machine-id:/etc/machine-id:ro  
# -v /etc/hostname:/etc/hostname:ro  
CMD journalctl --system -o short -f | nc --udp 172.17.42.1 5141  

