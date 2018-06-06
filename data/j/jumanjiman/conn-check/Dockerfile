FROM alpine:3.4  
  
# Which version of conn-check to install.  
# If you change this, you must also change circle.yml  
ENV VERSION 1.3.1  
  
RUN apk upgrade \--no-cache --available && \  
apk add \--no-cache \  
ca-certificates \  
openssl \  
python \  
py-setuptools \  
&& apk add \--no-cache -t devtools \  
alpine-sdk \  
libffi-dev \  
openssl-dev \  
python-dev \  
py-pip \  
yaml-dev \  
&& pip install -Iv conn-check==${VERSION} \  
&& apk del --purge devtools \  
&& adduser -D user  
  
COPY sample.yaml /etc/conn-check/  
  
USER user  
WORKDIR /home/user  
  
ENTRYPOINT ["conn-check"]  

