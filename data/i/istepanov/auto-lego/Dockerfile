FROM alpine:3.5  
MAINTAINER Ilya Stepanov <dev@ilyastepanov.com>  
  
ENV LEGO_VERSION v0.3.1  
ENV PYTHONUNBUFFERED 1  
RUN apk add --no-cache python3 docker openssl && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
pip3 install plumbum requests && \  
rm -r /root/.cache  
  
RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates && \  
mkdir -p /tmp/lego && cd /tmp/lego && \  
wget
https://github.com/xenolf/lego/releases/download/$LEGO_VERSION/lego_linux_amd64.tar.xz
&& \  
tar --xz -xvf lego_linux_amd64.tar.xz && ls && \  
cp lego/lego /usr/bin/lego && chmod +x /usr/bin/lego && \  
apk del build-dependencies && \  
cd / && rm -rf /tmp/lego  
  
ADD run.py /usr/bin/run.py  
RUN chmod +x /usr/bin/run.py  
  
CMD ["/usr/bin/run.py"]  

