FROM alpine:3.4  
MAINTAINER Mathieu Viossat <mathieu@viossat.fr>  
  
ENV DUPLICITY_VERSION 0.7.10  
  
RUN apk add --no-cache \  
ca-certificates \  
gnupg \  
librsync \  
py-pip \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libffi-dev \  
librsync-dev \  
linux-headers \  
musl-dev \  
openssl-dev \  
python-dev \  
wget \  
&& pip install --no-cache-dir \  
lockfile \  
pyrax \  
&& cd /tmp \  
&& wget -O duplicity.tar.gz
"https://launchpad.net/duplicity/0.7-series/$DUPLICITY_VERSION/+download/duplicity-$DUPLICITY_VERSION.tar.gz"
\  
&& tar xf duplicity.tar.gz \  
&& cd "duplicity-$DUPLICITY_VERSION" \  
&& python setup.py install \  
&& apk del .build-deps \  
&& rm -rf /tmp/*  
  
COPY entrypoint.sh /  
  
VOLUME /root/.cache/duplicity /etc/crontabs  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["crond", "-f"]  

