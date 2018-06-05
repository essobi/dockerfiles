FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG PYTHON_VERSION=2.7.14  
ARG PYINSTALLER_VERSION=3.2.1  
# we need wine for this all to work, so we'll use the PPA  
RUN set -x \  
&& dpkg --add-architecture i386 \  
&& apt-get update -qy \  
&& apt-get install -y python:i386 python2.7-minimal:i386 python2.7:i386
python-pip python-dev:i386 \  
&& apt-get clean  
  
# PYPI repository location  
ENV PYPI_URL=https://pypi.python.org/  
# PYPI index location  
ENV PYPI_INDEX_URL=https://pypi.python.org/simple  
  
# install pyinstaller  
RUN /usr/bin/pip install pyinstaller==$PYINSTALLER_VERSION  
  
# Make the src folder  
RUN mkdir /src  
VOLUME /src  
WORKDIR /src  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

