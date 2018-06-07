FROM alpine:latest  
RUN apk add --no-cache build-base python3-dev libffi-dev openssl-dev jq groff
libxml2-dev py3-lxml libxslt-dev && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
pip3 install aws awscli onelogin-aws-cli && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  
  

