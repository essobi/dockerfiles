FROM alpine:latest  
MAINTAINER Alex Pawlowski "pawlowski@kitcast.tv"  
  
RUN apk add \--no-cache bash build-base python python-dev openssl openssl-dev
libffi libffi-dev curl git zip unzip && \  
curl https://bootstrap.pypa.io/get-pip.py | python \- && \  
git clone -b develop https://github.com/kitcast/isign.git && \  
cd /isign && \  
python setup.py sdist && \  
pip install dist/*.tar.gz && \  
cd / && \  
rm -rf /isign && \  
pip uninstall -y pip setuptools wheel && \  
rm -rf /root/.cache/pip && \  
apk del --no-cache bash build-base python-dev openssl-dev libffi-dev curl git  
  
ENTRYPOINT ["/usr/bin/isign"]

