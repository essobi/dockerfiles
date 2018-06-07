FROM ubuntu:trusty  
LABEL maintainer="Khwunchai Jaengsawang <khwunchai.j@ku.th>"  
  
# Setting DEBIAN_FRONTEND=noninteractive  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common  
  
# Installing Java8  
RUN add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| sudo /usr/bin/debconf-set-selections \  
&& apt-get install -y oracle-java8-installer  
  
# Installing dependencies  
RUN wget http://public-
repo-1.hortonworks.com/HDP/ubuntu16/2.x/updates/2.6.4.0/hdp.list -O
/etc/apt/sources.list.d/hdp.repo \  
&& apt-get update \  
&& apt-get install --fix-missing -q -y \  
libkrb5-dev \  
libmysqlclient-dev \  
libssl-dev \  
libsasl2-dev \  
libsasl2-modules-gssapi-mit \  
libsqlite3-dev \  
libtidy-0.99-0 \  
libxml2-dev \  
libxslt-dev \  
libffi-dev \  
libldap2-dev \  
libgmp3-dev \  
libz-dev \  
python-dev \  
python-setuptools \  
python-psycopg2 \  
git \  
ant \  
gcc \  
g++ \  
make \  
maven \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# Installing Hue  
ENV HUE_VERSION=master  
  
RUN git clone \--depth 1 --branch=$HUE_VERSION
https://github.com/cloudera/hue.git  
RUN useradd -ms /bin/bash hue && chown -R hue hue  
  
USER hue  
WORKDIR hue  
RUN make apps  
EXPOSE 8888  
VOLUME /hue/desktop/  
CMD ["build/env/bin/hue", "runserver_plus", "0.0.0.0:8888"]

