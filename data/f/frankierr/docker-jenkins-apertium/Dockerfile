FROM jenkinsci/jenkins:latest  
MAINTAINER Frankie Robertson <frankie@robertson.name>  
  
USER root  
  
RUN apt-get update && apt-get install -y \  
wget \  
curl  
  
# Python 3  
RUN apt-get -f install -y virtualenv python-virtualenv python3-virtualenv  
RUN apt-get -f install -y python3  
RUN echo "deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu trusty main"
>> /etc/apt/sources.list.d/deadsnakes.list \  
&& echo "deb-src http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu trusty
main" >> /etc/apt/sources.list.d/deadsnakes.list \  
&& (gpg --keyserver keyserver.ubuntu.com \--recv-keys DB82666C || true) \  
&& gpg --export DB82666C | apt-key add \- \  
&& apt-get update \  
&& apt-get -f install -y python3.5 python3.5-dev  
  
# Apertium build requirements  
RUN apt-get -f install -y subversion build-essential pkg-config gawk libxml2 \  
libxml2-dev libxml2-utils xsltproc flex automake libtool libpcre3-dev \  
zlib1g zlib1g-dev  
  
# Apertium/lttoolbox/lex tools  
RUN svn co https://svn.code.sf.net/p/apertium/svn/trunk/lttoolbox/ \  
&& cd lttoolbox \  
&& ./autogen.sh \  
&& make \  
&& make install \  
&& ldconfig  
  
RUN svn co https://svn.code.sf.net/p/apertium/svn/trunk/apertium/ \  
&& cd apertium \  
&& ./autogen.sh \  
&& make \  
&& make install \  
&& ldconfig  
  
RUN svn co https://svn.code.sf.net/p/apertium/svn/trunk/apertium-lex-tools/ \  
&& cd apertium-lex-tools \  
&& ./autogen.sh \  
&& make \  
&& make install \  
&& ldconfig  
  
# Apertium-cleanstream  
RUN svn co https://svn.code.sf.net/p/apertium/svn/trunk/apertium-
tools/apertium-cleanstream \  
&& cd apertium-cleanstream \  
&& make \  
&& cp apertium-cleanstream /usr/local/bin  
  
# Building lxml takes ages so install it globally  
RUN apt-get -f install -y libxml2 libxml2-dev libxslt1.1 libxslt1-dev \  
&& wget https://bootstrap.pypa.io/get-pip.py \  
&& python3.5 get-pip.py \  
&& python3.5 -m pip install lxml==3.6.1  
  
USER jenkins  

