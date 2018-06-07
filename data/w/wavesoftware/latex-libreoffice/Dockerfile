FROM ubuntu:16.04  
MAINTAINER Krzysztof Suszyński <krzysztof.suszynski@wavesoftware.pl>  
  
RUN apt-get update && apt-get install -y \  
texlive-full \  
git \  
libreoffice \  
rake \  
ruby \  
ruby-dev \  
make \  
g++ \  
gcc \  
libffi-dev \  
python \  
python-pip \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip install Pygments  
RUN gem install bundler  

