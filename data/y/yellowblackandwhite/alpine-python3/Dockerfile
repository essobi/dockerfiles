FROM yellowblackandwhite/alpine-base  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
  
USER root  
COPY requirements.txt /tmp/  
  
RUN apk add \--no-cache \--virtual=build-dependencies python3 python3-dev
libffi libffi-dev wget ca-certificates && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \  
pip3 install setuptools --upgrade && \  
pip3 install --upgrade -r /tmp/requirements.txt && \  
apk del build-dependencies  
  
COPY pip_entry_point.sh /  
ENTRYPOINT ["/pip_entry_point.sh"]  
  
USER alpine  

