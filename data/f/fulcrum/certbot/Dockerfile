FROM fulcrum/alpine  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
# from https://github.com/xataz/dockerfiles/tree/master/letsencrypt  
ARG CERTBOT_VER=v0.18.2  
LABEL description="Letsencrypt based on alpine" \  
tags="latest 0.18.2 0.18" \  
build_ver="2017092001"  
  
RUN BUILD_DEPS="py-pip \  
gcc \  
musl-dev \  
python-dev \  
libffi-dev \  
openssl-dev" \  
&& apk add -U ${BUILD_DEPS} \  
py-pip \  
tini \  
dialog \  
python \  
&& pip install --no-cache virtualenv \  
&& virtualenv --no-site-packages -p python2 /usr/certbot/venv \  
&& /usr/certbot/venv/bin/pip install --no-cache-dir certbot==${CERTBOT_VER} \  
&& pip uninstall --no-cache-dir -y virtualenv \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/* /root/.cache/pip  
  
EXPOSE 80 443  
VOLUME /etc/letsencrypt/  
  
ENTRYPOINT ["/sbin/tini","--","/usr/certbot/venv/bin/certbot"]  
CMD ["--help"]  

