FROM alpine:3.6  
LABEL maintainer="Napat Chuangchunsong <https://github.com/napat>"  
LABEL Name="Certbot"  
LABEL Version="1.0"  
  
WORKDIR /opt/certbot  
ENV PATH /opt/certbot/venv/bin:$PATH  
  
RUN export BUILD_DEPS="git \  
build-base \  
libffi-dev \  
linux-headers \  
py-pip \  
python-dev" \  
&& apk -U upgrade \  
&& apk add dialog \  
python \  
openssl-dev \  
augeas-libs \  
${BUILD_DEPS} \  
  
&& pip --no-cache-dir install virtualenv \  
&& git clone https://github.com/letsencrypt/letsencrypt /opt/certbot/src \  
&& virtualenv --no-site-packages -p python2 /opt/certbot/venv \  
&& /opt/certbot/venv/bin/pip install \  
-e /opt/certbot/src/acme \  
-e /opt/certbot/src \  
-e /opt/certbot/src/certbot-apache \  
-e /opt/certbot/src/certbot-nginx \   
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/*  
  
  
VOLUME ["/etc/letsencrypt", "/usr/src/python"]  
  
COPY main.py /usr/src/  
COPY example /usr/src/python/  
  
CMD [ "python", "-u", "/usr/src/main.py" ]  

