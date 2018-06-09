FROM prcy/phalcon:3.x  
  
RUN \  
mkdir -p /var/cache/apt/archives/partial && \  
mkdir -p /var/log/apt && \  
mkdir -p /etc/supervisor/conf.d/ && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y python python-setuptools && \  
rm -rf /var/cache/apt/archives/partial && \  
rm -rf /var/log/apt && \  
easy_install pip && \  
pip install supervisor==3.0.1 && \  
echo "[supervisord]" > /etc/supervisor/supervisord.conf && \  
echo "[include]" >> /etc/supervisor/supervisord.conf && \  
echo "files = /etc/supervisor/conf.d/*.conf" >>
/etc/supervisor/supervisord.conf  
  
ADD wait-for-it.sh /usr/local/bin  
RUN ["chmod", "+x", "/usr/local/bin/wait-for-it.sh"]  
  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisor/supervisord.conf"]  

