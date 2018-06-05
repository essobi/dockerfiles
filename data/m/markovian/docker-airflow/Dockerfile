FROM continuumio/miniconda3  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
# Airflow  
ARG AIRFLOW_VERSION=1.7.1.3  
ARG AIRFLOW_REPO_URL=https://github.com/markovianhq/incubator-airflow.git  
ARG AIRFLOW_COMMIT=1a54fdc  
ENV AIRFLOW_HOME /usr/local/airflow  
  
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
libxml2-dev \  
libxslt1-dev \  
' \  
&& apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
$buildDeps \  
apt-utils \  
curl \  
netcat \  
locales \  
&& sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
&& pip install --upgrade pip \  
&& pip install pytz==2015.7 \  
&& pip install cryptography \  
&& pip install pyOpenSSL \  
&& pip install ndg-httpsclient \  
&& pip install pyasn1 \  
&& pip install psycopg2 \  
&& pip install requests \  
&& pip install 'google-api-python-client>=1.5.0,<1.6.0' \  
&& pip install 'oauth2client>=2.0.2,<2.1.0' \  
&& pip install httplib2 \  
&& pip install celery \  
&& pip install flower \  
&& git clone ${AIRFLOW_REPO_URL} \  
&& cd incubator-airflow \  
&& git checkout ${AIRFLOW_COMMIT} \  
&& pip install -e . \  
&& cd .. \  
&& apt-get remove --purge -yqq $buildDeps libpq-dev \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
WORKDIR ${AIRFLOW_HOME}  

