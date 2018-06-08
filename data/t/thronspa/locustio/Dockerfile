FROM alpine:3.4  
  
MAINTAINER Luca Agostini <agostini.luca@gmail.com>  
  
RUN apk add --update \  
bash \  
g++ \  
libstdc++ \  
nginx \  
python \  
python-dev \  
py-pip \  
py-setuptools && \  
rm -rf /var/cache/apk/* && \  
pip install --no-cache-dir --upgrade --force-reinstall \  
pip \  
pyzmq \  
locustio && \  
mkdir -p /run/nginx/  
  
COPY files/ /  
  
RUN chmod +x /etc/docker/start.sh  
  
CMD ["/etc/docker/start.sh"]  

