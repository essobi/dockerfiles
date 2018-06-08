FROM alpine:3.3  
MAINTAINER Cyprien <https://github.com/MisterCyp/dockerfiles>  
  
ENV UID=1000 GID=1000 WEBROOT=/rufy  
  
LABEL description="RuFy based on alpine" \  
build_ver="2016050301"  
  
RUN export BUILD_DEPS="git \  
py-pip \  
python-dev" \  
&& apk add -U python \  
supervisor \  
nginx \  
${BUILD_DEPS} \  
&& pip --no-cache-dir install virtualenv \  
&& git clone https://github.com/MisterCyp/RuFy.git /var/www/RuFy \  
&& virtualenv --no-site-packages -p python2.7 /var/www/RuFy/venv \  
&& /var/www/RuFy/venv/bin/pip install \  
-r /var/www/RuFy/requirements.txt \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/*  
  
COPY rootfs /  
RUN chmod +x /usr/local/bin/run.sh  
EXPOSE 80  
VOLUME /watch /var/www/RuFy/log /var/www/RuFy/db  
  
CMD ["sh","/usr/local/bin/run.sh"]  

