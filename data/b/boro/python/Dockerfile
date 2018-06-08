FROM python:3.6.4-alpine3.6  
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
make  
  
# Add Scripts  
ADD scripts/start.sh /start.sh  
ADD scripts/pull /usr/bin/pull  
ADD scripts/push /usr/bin/push  
  
RUN chmod 755 /usr/bin/pull && chmod 755 /usr/bin/push && chmod 755 /start.sh  
  
RUN mkdir /app  
CMD ["/start.sh"]

