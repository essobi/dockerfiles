FROM ubuntu:14.04  
  
MAINTAINER Mauricio Araya V.  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN true \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y build-essential git curl software-properties-common
libyaml-dev libssl-dev libffi-dev \  
&& apt-get install -y python2.7 libpython2.7-dev \  
&& apt-get install -y python-dev python-pip \  
&& pip install pip --upgrade \  
&& pip install virtualenv  
  
RUN true \  
&& mkdir -p /app/build \  
&& cd /app/build \  
&& virtualenv env \  
&& source env/bin/activate \  
&& pip install pip --upgrade \  
&& pip install requests[security] pyopenssl ndg-httpsclient pyasn1 \  
&& pip install flask zappa  
  
CMD ["/bin/bash"]  

