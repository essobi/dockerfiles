FROM debian:jessie  
MAINTAINER lucienchu<lucienchu@hotmail.com>  
  
#httpredir.debian.org  
#mirrors.163.com  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak \  
&& echo "deb http://httpredir.debian.org/debian/ jessie main non-free contrib"
>> /etc/apt/sources.list \  
&& echo "deb http://httpredir.debian.org/debian/ jessie-updates main non-free
contrib" >> /etc/apt/sources.list \  
&& echo "deb http://httpredir.debian.org/debian/ jessie-backports main non-
free contrib" >> /etc/apt/sources.list \  
&& echo "deb http://httpredir.debian.org/debian-security/ jessie/updates main
non-free contrib" >> /etc/apt/sources.list \  
&& apt-get update -q \  
&& apt-get upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y git-core cron  
  
VOLUME /data  
WORKDIR /app  
  
RUN git clone https://github.com/PPMESSAGE/ppmessage.git \  
&& cd /app/ppmessage/ppmessage/scripts/ \  
&& bash set-up-ppmessage-on-debian-or-ubuntu.sh  
  
RUN cd /tmp \  
&& curl --progress --remote-name http://nginx.org/download/nginx-1.9.15.tar.gz
\  
&& git clone https://github.com/vkholodkov/nginx-upload-module.git \  
&& cd nginx-upload-module && git checkout 2.2 && cd ../ \  
&& tar -xzvf nginx-1.9.15.tar.gz \  
&& cd nginx-1.9.15 \  
&& ./configure --with-http_ssl_module --add-module=../nginx-upload-module \  
&& make && make install \  
&& ln -s /usr/local/nginx/sbin/nginx /usr/bin/nginx  
  
COPY config.json /app/ppmessage/ppmessage/bootstrap/  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY crontab /etc/cron.d/  
COPY init.py /app/ppmessage/  
COPY nginx.conf /usr/local/nginx/conf/nginx.conf  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
#ENTRYPOINT ["/bin/bash"]

