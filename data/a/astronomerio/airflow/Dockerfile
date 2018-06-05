FROM debian:8.6  
MAINTAINER schnie <greg@astronomer.io>  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
# Airflow  
ARG AIRFLOW_VERSION=1.7.1.3  
ENV AIRFLOW_HOME /airflow_home  
  
# Define en_US.  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_MESSAGES en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
# Install dependencies.  
RUN set -ex \  
&& buildDeps=' \  
python-pip \  
python-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libffi-dev \  
build-essential \  
libblas-dev \  
liblapack-dev \  
git \  
' \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF \  
&& echo "deb http://repos.mesosphere.com/ubuntu vivid main" >
/etc/apt/sources.list.d/mesosphere.list \  
&& echo "deb http://http.debian.net/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list \  
&& apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
$buildDeps \  
apt-utils \  
curl \  
netcat \  
locales \  
dnsutils \  
mesos \  
supervisor \  
&& apt-get install -yqq -t jessie-backports python-requests cython libpq-dev \  
&& sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
# && useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \  
&& pip install pytz==2015.7 \  
&& pip install cryptography \  
&& pip install pyOpenSSL \  
&& pip install ndg-httpsclient \  
&& pip install pyasn1 \  
&& pip install protobuf \  
&& pip install pydash==3.4.3 \  
&& pip install pymongo==3.2.2 \  
&& pip install stringcase==1.0.6 \  
&& pip install fn==0.4.3 \  
&& pip install docker-py==1.8.1 \  
&& pip install python-decouple==3.0 \  
&& pip install nose2==0.6.5 \  
&& pip install cov-core==1.15.0 \  
&& pip install coverage==4.2 \  
&& pip install pycodestyle==2.2.0 \  
  
&& pip install git+https://github.com/astronomerio/incubator-
airflow@astronomer-fixes#egg=incubator-airflow[s3,postgres,password] \  
# && pip install -e /incubator-airflow \  
# && pip install airflow==$AIRFLOW_VERSION \  
  
&& apt-get remove --purge -yqq $buildDeps libpq-dev \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
# Set python path so airflow can find pip installed packages.  
ENV PYTHONPATH=${PYTHONPATH}:/usr/lib/python2.7/site-packages/  
  
# Add supervisor configs.  
ADD config /etc/supervisor/conf.d/  
  
# Add scripts.  
ADD script script  
  
# Set airflow home.  
ADD airflow_home ${AIRFLOW_HOME}/  
  
EXPOSE 8080 5555 8793  
WORKDIR ${AIRFLOW_HOME}  
ENTRYPOINT ["/script/entrypoint.sh"]  

