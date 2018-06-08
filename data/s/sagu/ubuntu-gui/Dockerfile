FROM sagu/ubuntu-sshd:16.04  
RUN apt install firefox -y && echo "DISPLAY=192.168.99.1:0" >>
/etc/environment  
ENV DISPLAY=192.168.99.1:0  
ENTRYPOINT apt-get update -q && /usr/sbin/sshd -D

