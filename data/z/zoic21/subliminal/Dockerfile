FROM debian:jessie  
  
MAINTAINER loic  
  
ENV SHELL_ROOT_PASSWORD root  
  
RUN apt-get update && apt-get install -y \  
wget \  
ntp \  
unzip \  
curl \  
supervisor \  
tar \  
python \  
ca-certificates \  
git \  
python-pip \  
cron  
  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ADD subliminal.py /root/subliminal.py  
ADD init.sh /root/init.sh  
RUN chmod +x /root/init.sh  
CMD ["/root/init.sh"]  

