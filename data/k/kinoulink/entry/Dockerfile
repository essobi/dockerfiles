FROM phusion/baseimage:0.9.19  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
nginx \  
wget  
  
#RUN apt-get upgrade -y libc6:amd64  
RUN apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp && \  
wget https://github.com/jwilder/docker-gen/releases/download/0.7.3/docker-gen-
linux-amd64-0.7.3.tar.gz && \  
tar xvzf docker-gen-linux-amd64-0.7.3.tar.gz && \  
mv docker-gen /usr/local/bin/docker-gen && \  
chmod +x /usr/local/bin/docker-gen  
  
ADD service/gen /etc/service/gen  
ADD service/nginx /etc/service/nginx  
ADD www /var/www  
  
RUN chown -R www-data /var/www && \  
rm -rf /etc/service/sys* /etc/service/cron /etc/service/sshd  
  
EXPOSE 80  
EXPOSE 443  

