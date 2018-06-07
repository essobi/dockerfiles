FROM ubuntu:xenial  
  
# RUN apt-get update && apt-get install -y supervisor gcc python-pip python-
dev curl lsof net-tools vim-nox strace sudo --no-install-recommends  
RUN apt-get update && apt-get install -y supervisor python-pip python-dev curl
lsof net-tools sudo --no-install-recommends  
RUN apt-get install -y gcc autoconf python-setuptools --no-install-recommends  
  
RUN pip install --upgrade pip  
RUN pip install obfsproxy  
  
RUN apt-get install software-properties-common -y --no-install-recommends  
RUN add-apt-repository ppa:max-c-lv/shadowsocks-libev  
RUN apt-get update  
RUN apt-get install -y shadowsocks-libev --no-install-recommends  
RUN mkdir -p /etc/shadowsocks  
ADD files/client.json /etc/shadowsocks/  
  
ADD files/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
ADD files/supervisor/shadowsocks-client.ini /etc/supervisor/conf.d/  
ADD files/supervisor/obfsproxy-client.ini /etc/supervisor/conf.d/  
  
ADD run.sh /run.sh  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 7000  
CMD [ "/run.sh"]  
  

