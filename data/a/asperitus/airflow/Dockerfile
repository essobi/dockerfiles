##  
FROM python:3.6-slim  
MAINTAINER Qiang Li  
  
#  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
# Airflow  
ARG AIRFLOW_VERSION=1.8.1  
# Define en_US.  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_MESSAGES en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN set -ex \  
&& buildDeps=' \  
python3-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libffi-dev \  
build-essential \  
libblas-dev \  
liblapack-dev \  
libpq-dev \  
git \  
' \  
&& apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
$buildDeps \  
apt-utils \  
curl \  
netcat \  
python3-pip \  
python3-requests \  
sudo \  
locales \  
&& sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
&& python -m pip install -U pip setuptools wheel \  
&& pip install Cython \  
&& pip install pytz \  
&& pip install pyOpenSSL \  
&& pip install ndg-httpsclient \  
&& pip install pyasn1 \  
&& pip install apache-
airflow[celery,crypto,jdbc,postgres,slack]==$AIRFLOW_VERSION \  
&& pip install celery[redis]==3.1.17 \  
&& apt-get remove --purge -yqq $buildDeps \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
##  
RUN ln -sf bash /bin/sh  
  
##  
ARG AIRFLOW_HOME=/app  
  
WORKDIR ${AIRFLOW_HOME}  
  
RUN useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \  
&& chown -R airflow: ${AIRFLOW_HOME}  
  
USER airflow  
  
##  
EXPOSE 8080 5555 8793  
#  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

