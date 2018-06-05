FROM iron/python:2.7  
MAINTAINER James Gregory <james@jagregory.com>  
  
RUN apk update && \  
apk add curl && \  
curl -sS https://bootstrap.pypa.io/get-pip.py | python && \  
apk del curl && \  
pip install aws-amicleaner && \  
python -m pip uninstall pip setuptools -y && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["amicleaner"]  
CMD ["-h"]  

