FROM upclose/python3  
  
RUN wget -qO- https://github.com/Rushmorefm/alpine-
packages/releases/download/v0.2/testing.tar.xz | tar xJ \  
&& apk \--allow-untrusted -X /testing -X
http://dl-2.alpinelinux.org/alpine/edge/testing -U add \  
python35-dev \  
binutils \  
libc-dev \  
gcc \  
fortify-headers \  
&& rm -rf /testing /var/cache/apk/* \  
&& pip3 install \--no-cache virtualenv  
  
# installing certifi fixes OpenSSL 1.0.2 issues with some certificates  
RUN virtualenv /wheel_venv && /wheel_venv/bin/pip install \--upgrade certifi
devpi-client wheel  

