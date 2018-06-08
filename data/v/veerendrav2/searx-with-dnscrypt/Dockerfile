FROM alpine:3.6  
MAINTAINER Veerendra Kakumanu  
ARG VERSION=0.12.0  
ENV BASE_URL=False IMAGE_PROXY=False UID=991 GID=991  
RUN apk -U upgrade \  
&& apk add -t build-dependencies \  
build-base \  
python-dev \  
libffi-dev \  
libxslt-dev \  
libxml2-dev \  
openssl-dev \  
tar \  
ca-certificates \  
&& apk add \  
dnscrypt-proxy-setup \  
su-exec \  
python \  
libxml2 \  
libxslt \  
openssl \  
tini \  
py2-pip \  
&& mkdir /usr/local/searx && cd /usr/local/searx \  
&& wget -qO- https://github.com/asciimoo/searx/archive/v${VERSION}.tar.gz |
tar xz --strip 1 \  
&& pip install --no-cache -r requirements.txt \  
&& sed -i "s/127.0.0.1/0.0.0.0/g" searx/settings.yml \  
&& apk del build-dependencies \  
&& rm -f /var/cache/apk/*  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
RUN wget -O /usr/local/dnscrypt-resolvers.csv
https://raw.githubusercontent.com/jedisct1/dnscrypt-proxy/master/dnscrypt-
resolvers.csv --no-check-certificate  
EXPOSE 8888  
CMD ["run.sh"]

