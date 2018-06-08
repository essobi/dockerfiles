FROM debian:8  
RUN apt-get update && \  
apt-get install wget unzip python apache2 python-gtk2 libnss3-tools -y && \  
wget -O /root/goproxy.zip https://raw.githubusercontent.com/mixool/docker-
gip/goproxy/goproxy.zip && \  
unzip -d /root /root/goproxy.zip && \  
chmod +x /root/goproxy/goproxy && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/www/html/* /root/goproxy.zip && \  
ln -sv /root/goproxy /var/www/html  
  
COPY run.sh /root/run.sh  
COPY gae.user.json /root/goproxy/gae.user.json  
COPY php.user.json /root/goproxy/php.user.json  
  
RUN chmod +x /root/run.sh  
  
EXPOSE 80 8087 8088  
CMD ["/root/run.sh"]  

