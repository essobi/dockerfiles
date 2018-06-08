From debian:latest  
LABEL maintainer ant <git@manchestermonkey.co.uk>  
  
  
RUN apt-get update -qq && apt-get install -qq python-setuptools \  
ca-certificates curl wget build-essential python-dev \  
python-cffi libffi-dev libxslt1-dev zlib1g-dev \  
libxslt1-dev zlib1g-dev libssl-dev libxslt1-dev zlib1g-dev \  
&& easy_install pip \  
&& pip install --upgrade cffi \  
&& pip install magic-wormhole \  
&& mkdir /tfr \  
&& rm /usr/share/doc -Rf \  
&& rm /usr/share/man -Rf \  
&& rm /var/lib/apt/lists -Rf \  
  
  
WORKDIR /tfr  
  
##ENTRYPOINT ["wormhole"]  

