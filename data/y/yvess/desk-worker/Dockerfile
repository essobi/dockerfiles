FROM alpine:3.4  
MAINTAINER Yves Serrano <y@yas.ch>  
  
RUN apk add --no-cache \  
curl \  
python \  
py-pip \  
make \  
readline \  
openssl \  
wget \  
python-dev \  
libxml2 \  
libxslt \  
openldap \  
libffi \  
pango \  
bind-tools \  
ttf-freefont  
  
# s6 overlay  
RUN curl -Ls -o /tmp/s6-overlay.tar.gz https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz && \  
tar xvfz /tmp/s6-overlay.tar.gz -C / && \  
rm -f /tmp/s6-overlay.tar.gz  
  
ADD requirements.txt /tmp/requirements.txt  
RUN apk add --no-cache \  
git \  
gcc \  
g++ \  
openssl-dev \  
readline-dev \  
libxml2-dev \  
libxslt-dev \  
openldap-dev \  
libffi-dev \  
pango-dev \  
cairo \  
pango-dev \  
&& \  
cat /tmp/requirements.txt |grep -v "^#"| xargs -n 1 pip install && \  
apk del \  
gcc \  
g++ \  
openssl-dev \  
readline-dev \  
libxml2-dev \  
libxslt-dev \  
openldap-dev \  
libffi-dev \  
pango-dev \  
&& \  
rm -rf /var/cache/apk/* /tmp/* /var/tmp/*  
ADD ./etc/ /etc/  
ENV WORKER_TYPE foreman  
ENTRYPOINT ["/init"]  

