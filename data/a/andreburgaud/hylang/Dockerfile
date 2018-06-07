FROM alpine:3.7  
ENV HYLANG_VERSION=0.14.0  
LABEL hylang.version=$HYLANG_VERSION  
LABEL python.version=3.6.3-r9  
  
RUN apk add --no-cache python3=3.6.3-r9 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools --no-cache-dir && \  
pip3 install hy==$HYLANG_VERSION \--no-cache-dir && \  
if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  
  
CMD ["hy"]  

