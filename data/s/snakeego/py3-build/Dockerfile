FROM python:3.5-alpine  
# Setup PyInstaller  
RUN apk \--update \--no-cache add \  
zlib-dev \  
musl-dev \  
git \  
pwgen \  
build-base \  
&& pip install \--upgrade pip \  
&& git clone https://github.com/pyinstaller/pyinstaller.git /tmp/pyinstaller \  
&& cd /tmp/pyinstaller/bootloader \  
&& python ./waf configure \--no-lsb all \  
&& pip install .. \  
&& cd \- \  
&& rm -rf /tmp/pyinstaller  
# ldd fix for correct pyInstaller lib detection  
RUN mv /usr/bin/ldd /bin/ldd \  
&& echo '#!/bin/sh' > /usr/bin/ldd \  
&& echo 'exec /bin/ldd "$@" | \  
sed -r "s/([^[:space:]]+) => ldd/\1 => \/lib\/\1/g" | \  
sed -r "s/ldd \\(.*\\)//g"' | sed 's/^[\t ]*//g' >> /usr/bin/ldd \  
&& chmod +x /usr/bin/ldd  
  
RUN mkdir -p /app/project /app/data /app/build  
WORKDIR /app/project  
  
VOLUME ["/app/project", "/app/data", "/app/build"]  
ENTRYPOINT ["/usr/bin/make"]  
  

