FROM alpine:latest  
RUN apk add \--no-cache --update \  
python py-pip git wget autoconf automake build-base linux-headers python-dev
supervisor && \  
pip install --upgrade pip setuptools tornado u-msgpack-python jinja2 chardet
requests pbkdf2 && \  
mkdir -p /opt && \  
cd /opt && \  
git clone https://github.com/binux/qiandao \  
\--depth 1 \--branch master --single-branch && \  
cd qiandao && \  
apk del build-base linux-headers python-dev autoconf automake wget py-pip && \  
rm -rf /var/cache/apk/*  
  
ENV PORT 80  
  
EXPOSE $PORT  
  
ENTRYPOINT python /opt/qiandao/run.py  

