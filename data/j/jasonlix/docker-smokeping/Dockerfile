FROM ubuntu:xenial  
  
MAINTAINER Smokeping "jasonlix5@gmail.com"  
  
ENV SMOKEPING_VERSION 2.6.11-2  
  
RUN apt-get update && \  
apt-get install --no-install-recommends --no-install-suggests -y \  
smokeping=${SMOKEPING_VERSION} \  
nginx \  
fcgiwrap \  
openssh-client \  
curl \  
vim \  
fping \  
echoping \  
dnsutils \  
sendmail && \  
rm -rf /var/lib/apt/lists/*  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
ADD ./conf/smokeping /etc/nginx/sites-available/smokeping  
ADD ./start.sh /start.sh  
  
RUN sed -i 's/^DAEMON_USER=smokeping/DAEMON_USER=www-data/g'
/etc/init.d/smokeping && \  
chown www-data.www-data /etc/smokeping/smokeping_secrets && \  
chown -R www-data.www-data /var/lib/smokeping/ && \  
ln -s /usr/share/doc/fcgiwrap/examples/nginx.conf /etc/nginx/fcgiwrap.conf &&
\  
ln -s /usr/lib/cgi-bin/smokeping.cgi /usr/share/smokeping/www/smokeping.cgi &&
\  
ln -s /usr/share/smokeping/www /usr/share/smokeping/www/smokeping && \  
rm -f /etc/nginx/sites-enabled/default && \  
ln -s /etc/nginx/sites-available/smokeping /etc/nginx/sites-enabled/smokeping  
  
EXPOSE 80 443  
  
CMD ["/bin/sh","/start.sh"]  

