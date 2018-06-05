# VERSION 1.7.1.3  
# AUTHOR: Jean Baptiste Favre  
# DESCRIPTION: Basic all-in-one Airflow container  
# BUILD: docker build --rm -t jbfavre/airflow-light  
# SOURCE: https://github.com/jbfavre/docker-airflow-light  
FROM debian:jessie  
MAINTAINER Jean Baptiste Favre <docker@jbfavre.org>  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
# Airflow  
ARG AIRFLOW_VERSION=1.7.1.3  
ENV AIRFLOW_HOME /usr/local/airflow  
  
# Define en_US.  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_MESSAGES en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Python  
ENV PYTHON_EGG_CACHE /tmp/.python-eggs  
  
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
' \  
&& echo "deb http://http.debian.net/debian jessie-backports main"
>/etc/apt/sources.list.d/backports.list \  
&& apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
$buildDeps \  
apt-utils \  
curl \  
netcat \  
locales \  
&& apt-get install -yqq -t jessie-backports python-requests supervisor \  
&& sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
&& useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \  
&& pip install pytz==2015.7 \  
&& pip install cryptography \  
&& pip install pyOpenSSL \  
&& pip install ndg-httpsclient \  
&& pip install pyasn1 \  
&& pip install airflow[hive]==$AIRFLOW_VERSION \  
&& chown airflow: -R /var/log/supervisor/ \  
&& apt-get remove --purge -yqq $buildDeps \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
COPY script/entrypoint.sh ${AIRFLOW_HOME}/entrypoint.sh  
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg  
COPY config/supervisord.conf /etc/supervisor/supervisord.conf  
COPY config/supervisor-airflow.conf /etc/supervisor/conf.d/airflow.conf  
  
RUN chown -R airflow: ${AIRFLOW_HOME} \  
&& chmod +x ${AIRFLOW_HOME}/entrypoint.sh  
  
EXPOSE 8080 5555 8793  
USER airflow  
WORKDIR ${AIRFLOW_HOME}  
ENTRYPOINT ["./entrypoint.sh"]  

