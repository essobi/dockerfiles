FROM node:8.10.0-alpine  
  
MAINTAINER boro <docker@bo.ro>  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && apk update && \  
apk add --no-cache bash \  
openssh-client \  
wget \  
supervisor \  
curl \  
bc \  
gcc \  
musl-dev \  
linux-headers \  
python \  
python-dev \  
py-pip \  
augeas-dev \  
openssl-dev \  
libffi-dev \  
ca-certificates \  
dialog \  
git \  
make \  
libnetfilter_queue-dev && \  
mkdir -p /var/www/app && \  
mkdir -p /var/log/supervisor  
  
# Install Freebind  
RUN mkdir /home/freebind-source && git clone
https://github.com/blechschmidt/freebind.git /home/freebind-source/.  
RUN cd /home/freebind-source && make install  
RUN rm -rf /home/freebind-source  
  
ADD conf/supervisord.conf /etc/supervisord.conf  
  
# Add Scripts  
ADD scripts/start.sh /start.sh  
ADD scripts/pull /usr/bin/pull  
ADD scripts/push /usr/bin/push  
RUN chmod 755 /usr/bin/pull && chmod 755 /usr/bin/push && chmod 755 /start.sh  
  
# copy in code  
ADD src/ /var/www/html/  
RUN mkdir -p /var/log/node/  
  
VOLUME /var/www/html/  
  
#CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  
CMD ["/start.sh"]  

