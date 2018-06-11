FROM ubuntu:xenial  
MAINTAINER brian.wojtczak@1and1.co.uk  
ARG DEBIAN_FRONTEND=noninteractive  
COPY files/ /  
RUN \  
apt-get -y update && apt-get -y upgrade && \  
apt-get -o Dpkg::Options::=--force-confdef -y install supervisor curl netcat
wget telnet vim bzip2 ssmtp locales python-pip && \  
locale-gen en_GB.utf8 en_US.utf8 es_ES.utf8 de_DE.UTF-8 && \  
mkdir --mode 777 -p /var/log/supervisor && \  
chmod -R 777 /var/run /var/log /etc/ssmtp /etc/passwd /etc/group && \  
mkdir --mode 777 -p /tmp/sockets && \  
chmod -R 755 /init /hooks && \  
chmod 755 /etc/supervisor/exit_on_fatal.py && \  
cd /opt/configurability/src/ && \  
pip --no-cache install --upgrade pip && \  
pip --no-cache install --upgrade PyYAML && \  
pip --no-cache install --upgrade . && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
ENV \  
SUPERVISORD_EXIT_ON_FATAL=1 \  
LC_ALL=en_GB.UTF-8 \  
LANG=en_GB.UTF-8 \  
LANGUAGE=en_GB.UTF-8 \  
SMTP_USER="" \  
SMTP_PASS="" \  
SMTP_DOMAIN="" \  
SMTP_RELAYHOST=""  
ENTRYPOINT ["/bin/bash", "-e", "/init/entrypoint"]  
CMD ["run"]  

