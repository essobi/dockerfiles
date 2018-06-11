FROM alpine:latest  
MAINTAINER m3adow  
  
# Long command to keep the FS deltas small  
RUN apk --update add python \  
python-dev \  
py-setuptools \  
py-pip \  
openssl-dev \  
openssl \  
musl-dev \  
gcc \  
libffi-dev \  
darkhttpd \  
&& wget -qO- https://codeload.github.com/kuba/simp_le/tar.gz/master | tar xz \  
&& pip install -e /simp_le-master/ \  
&& mkdir /certs \  
&& apk --purge del musl-dev openssl-dev libffi-dev gcc python-dev py-pip  
WORKDIR /certs  
COPY ["./startme.sh", "/usr/local/bin/"]  
ENTRYPOINT ["/usr/local/bin/startme.sh"]  

