# VERSION 1.7.0  
# AUTHOR: Matthieu "Puckel_" Roisil  
# DESCRIPTION: Basic Airflow container  
# BUILD: docker build --rm -t jwmarshall/docker-airflow  
# SOURCE: https://github.com/jwmarshall/docker-airflow  
# FROM ubuntu:14.04  
FROM ruimashita/numpy  
#FROM debian:jessie  
MAINTAINER Yu You  
  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
ENV INITRD No  
ENV AIRFLOW_VERSION 1.7.1.3  
ENV AIRFLOW_HOME /usr/local/airflow  
ENV PYTHONLIBPATH /usr/lib/python2.7/dist-packages  
  
# Add airflow user  
RUN useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow  
  
# Define en_US.  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_MESSAGES en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update -y \  
#echo "deb http://http.debian.net/debian jessie-backports main"
>/etc/apt/sources.list.d/backports.list \  
# && apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
ca-certificates \  
apt-utils\  
netcat \  
curl \  
python-pip \  
python-dev \  
libpq-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libffi-dev \  
build-essential \  
locales \  
# && apt-get install -yqq -t jessie-backports python-requests \  
# && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& update-locale LANG=en_US.utf8 LC_ALL=en_US.utf8 \  
# && useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \  
&& pip install pytz==2015.7 \  
&& pip install cryptography \  
&& pip install pyOpenSSL \  
&& pip install ndg-httpsclient \  
&& pip install pyasn1 \  
&& pip install airflow==${AIRFLOW_VERSION} \  
&& pip install airflow[celery]==${AIRFLOW_VERSION} \  
&& pip install airflow[postgres]==${AIRFLOW_VERSION} \  
&& pip install --install-option="--install-purelib=$PYTHONLIBPATH"
celery[redis] \  
&& apt-get remove --purge -yqq build-essential python-pip python-dev
libmysqlclient-dev libkrb5-dev libsasl2-dev libssl-dev libffi-dev \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
ADD script/entrypoint.sh ${AIRFLOW_HOME}/entrypoint.sh  
ADD config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg  
  
RUN \  
chown -R airflow: ${AIRFLOW_HOME} \  
&& chmod +x ${AIRFLOW_HOME}/entrypoint.sh  
  
EXPOSE 8080 5555 8793  
USER airflow  
WORKDIR ${AIRFLOW_HOME}  
ENTRYPOINT ["./entrypoint.sh"]  

