# VERSION 1.9  
# AUTHOR: Georgios Georgiadis  
# DESCRIPTION: Airflow container  
  
FROM python:3.5-slim  
MAINTAINER Yieldr  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
# Airflow  
ARG AIRFLOW_VERSION=1.9  
ARG AIRFLOW_HOME=/usr/local/airflow  
  
# Define en_US.  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LC_CTYPE en_US.UTF-8  
ENV LC_MESSAGES en_US.UTF-8  
  
RUN set -ex \  
&& buildDeps=' \  
python3-dev \  
libkrb5-dev \  
libsasl2-modules \  
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
&& apt-get upgrade -yqq \  
&& apt-get install -yqq --no-install-recommends \  
$buildDeps \  
python3-pip \  
python3-requests \  
mysql-client \  
mysql-server \  
libmysqlclient-dev \  
apt-utils \  
curl \  
rsync \  
netcat \  
locales \  
&& sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
&& useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \  
&& usermod -a -G sudo airflow \  
&& pip install -U pip setuptools wheel \  
&& pip install Cython \  
&& pip install pytz \  
&& pip install pyOpenSSL \  
&& pip install ndg-httpsclient \  
&& pip install pyasn1 \  
&& pip install pymysql \  
&& pip install flower \  
&& pip install mysqlclient \  
&& pip install boto3 \  
&& pip install boto \  
&& pip install apache-
airflow[s3,slack,crypto,celery,mysql,postgres,jdbc]==$AIRFLOW_VERSION \  
&& pip install celery[redis]==4.0.2 \  
&& pip install thrift_sasl \  
&& pip install unicodecsv==0.14.1 \  
&& pip install impyla==0.14.1 \  
&& pip install pyhive==0.5.1 \  
&& apt-get purge --auto-remove -yqq $buildDeps \  
&& apt-get autoremove -yqq --purge \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
COPY script/entrypoint.sh /entrypoint.sh  
  
# Move cfg file  
RUN mkdir ${AIRFLOW_HOME}/config  
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg  
  
RUN mkdir /usr/local/logs  
RUN chmod -R 777 /usr/local/logs  
  
RUN chown -R airflow: ${AIRFLOW_HOME}  
  
EXPOSE 8080 5555 8793  
#USER airflow  
#WORKDIR ${AIRFLOW_HOME}  
#ENTRYPOINT ["/entrypoint.sh"]  

