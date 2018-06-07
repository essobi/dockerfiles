FROM ubuntu:14.04  
MAINTAINER devteam@level12.io  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# map to the source code of the app  
VOLUME /opt/src  
# map to the CI artificates directory  
VOLUME /opt/src/.ci/artifacts  
# map to the CI test reports directory  
VOLUME /opt/src/.ci/test-reports  
  
RUN echo 'deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu trusty main'
>> /etc/apt/sources.list.d/python.list \  
&& apt-key adv \--keyserver keyserver.ubuntu.com \--recv-keys DB82666C \  
&& apt-get update -q \  
&& apt-get install -y curl git \  
python2.7 python2.7-dev libpython2.7-dev \  
python3.5 python3.5-dev libpython3.5-dev \  
python3.6 python3.6-dev libpython3.6-dev \  
&& curl -fSL "https://bootstrap.pypa.io/get-pip.py" -o get-pip.py \  
&& python2.7 get-pip.py \  
&& python3.4 get-pip.py \  
&& python3.5 get-pip.py \  
&& python3.6 get-pip.py \  
&& rm get-pip.py \  
&& rm -rf /var/lib/apt/lists/*  
  
# need these libraries for lxml, PyQuery, and dbus for Keyring  
RUN apt-get update && apt-get install -y \  
libfreetype6 \  
libjpeg-turbo8 \  
libpq5 \  
libxml2 \  
libxslt1.1 \  
libffi6 \  
libcairo2 \  
libpango1.0 \  
libtiff5 \  
libdbus-glib-1-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# install postgres client for migration testing  
RUN apt-get update && apt-get install -y wget \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list.d/pgdg.list \  
&& wget \--quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add \- \  
&& apt-get update \  
&& apt-get install -y postgresql-client-9.6 \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt/src  
ENTRYPOINT ["/bin/bash", "/opt/src/docker-entry"]  

