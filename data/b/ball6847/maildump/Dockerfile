FROM alpine:3.3  
MAINTAINER ball6847@gmail.com  
  
ADD . /src  
  
RUN apk add --update --no-cache \  
bash \  
build-base \  
python-dev \  
py-pip && \  
cd /src && \  
pip install -r requirements.txt && \  
webassets -m maildump.web build --production && \  
python setup.py build install && \  
apk del build-base && \  
rm -rf /var/cache/apk/* /root/.cache /src  
  
EXPOSE 1080 1025  
  
ENTRYPOINT [ "maildump", "-fn", "--smtp-ip", "0.0.0.0", "--http-ip", "0.0.0.0"
]  
  

