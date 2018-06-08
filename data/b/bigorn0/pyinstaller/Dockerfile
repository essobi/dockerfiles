# Shamely taken from https://github.com/six8/pyinstaller-alpine  
# but based on latest alpine 3.5  
# Official Python base image is needed or some applications will segfault.  
FROM bigorn0/python:alpine-3.5  
# PyInstaller needs zlib-dev, gcc, libc-dev, and musl-dev  
RUN apk --update --no-cache add \  
zlib-dev \  
musl-dev \  
libc-dev \  
gcc \  
git \  
pwgen \  
&& pip install --upgrade pip  
  
# Install pycrypto so --key can be used with PyInstaller  
RUN pip install pycrypto  
  
# Build bootloader for alpine  
RUN git clone https://github.com/pyinstaller/pyinstaller.git /tmp/pyinstaller
\  
&& cd /tmp/pyinstaller/bootloader \  
&& python ./waf configure --no-lsb all \  
&& pip install .. \  
&& rm -Rf /tmp/pyinstaller  
  
WORKDIR /src  
  
COPY ./bin /pyinstaller  
  
ENTRYPOINT [ "/pyinstaller/pyinstaller.sh" ]  

