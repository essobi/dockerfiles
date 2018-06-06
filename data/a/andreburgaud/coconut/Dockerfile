FROM alpine:3.6  
  
ENV COCONUT_VERSION=1.3.1  
  
LABEL coconut.version=$COCONUT_VERSION python.version=3.6.1-r3  
  
RUN apk add --no-cache zeromq freetype libpng python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --no-cache-dir --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -sf /usr/bin/pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  
  
RUN apk --no-cache add --virtual build-dependencies \  
gcc \  
g++ \  
libffi-dev \  
freetype-dev \  
libpng-dev \  
linux-headers \  
musl-dev \  
openssl-dev \  
python3-dev \  
zeromq-dev && \  
pip install --no-cache-dir coconut[all]==$COCONUT_VERSION && \  
pip install --no-cache-dir --trusted-host pypi.python.org numpy && \  
pip install --no-cache-dir --upgrade matplotlib && \  
apk del build-dependencies  
  
# Create dedicated jupyter user  
RUN addgroup -S jupyter && adduser -S -G jupyter jupyter  
  
WORKDIR /notebooks  
  
EXPOSE 8888  
  
CMD ["coconut", "--target", "36"]  
  
USER jupyter  

