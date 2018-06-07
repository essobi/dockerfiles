FROM alpine:latest  
MAINTAINER m3adow  
  
# Long command to keep the FS deltas small  
RUN apk add --no-cache \  
python \  
py-setuptools \  
py2-pip \  
openssl \  
darkhttpd \  
ca-certificates \  
git \  
&& apk add --no-cache --virtual build_deps \  
musl-dev \  
openssl-dev \  
libffi-dev \  
gcc \  
python-dev \  
&& pip install git+https://github.com/zenhack/simp_le/ \  
&& mkdir /certs \  
&& apk --purge del build_deps \  
&& rm -rf /root/.cache  
WORKDIR /certs  
COPY ["./startme.sh", "/usr/local/bin/"]  
ENTRYPOINT ["/usr/local/bin/startme.sh"]  

