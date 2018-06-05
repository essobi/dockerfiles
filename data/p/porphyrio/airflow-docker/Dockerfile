# VERSION 1.0  
# AUTHOR: Porphyrio  
# DESCRIPTION: airflow container  
# BUILD: docker build --rm -t porphyrio/airflow-docker:latest .  
  
FROM debian:wheezy  
MAINTAINER porhyrio  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
# Work around initramfs-tools running on kernel 'upgrade':
<http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>  
ENV INITRD No  
  
ENV AIRFLOW_VERSION 1.6.1  
ENV AIRFLOW_HOME /root/airflow  
ENV C_FORCE_ROOT true  
ENV PYTHONLIBPATH /usr/lib/python2.7/dist-packages  
ENV TZ Europe/Brussels  
  
VOLUME $AIRFLOW_HOME  
  
RUN apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
netcat \  
curl \  
git \  
python-pip \  
python-dev \  
libmysqlclient-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libffi-dev \  
build-essential \  
&& git config --global http.sslVerify false \  
&& mkdir -p $AIRFLOW_HOME/logs \  
&& mkdir $AIRFLOW_HOME/dags \  
&& pip install \--install-option="--install-purelib=$PYTHONLIBPATH"
cryptography \  
&& pip install \--install-option="--install-purelib=$PYTHONLIBPATH"
airflow==${AIRFLOW_VERSION} \  
&& pip install \--install-option="--install-purelib=$PYTHONLIBPATH"
airflow[mysql]==${AIRFLOW_VERSION} \  
&& pip install \--install-option="--install-purelib=$PYTHONLIBPATH"
airflow[s3]==${AIRFLOW_VERSION} \  
&& pip install \--install-option="--install-purelib=$PYTHONLIBPATH"
airflow[celery]==${AIRFLOW_VERSION} \  
&& pip install \--install-option="--install-purelib=$PYTHONLIBPATH"
airflow[async]==${AIRFLOW_VERSION} \  
&& pip install \--install-option="--install-purelib=$PYTHONLIBPATH"
https://github.com/diyan/pywinrm/archive/master.zip#egg=pywinrm \  
&& pip install \--install-option="--install-purelib=$PYTHONLIBPATH" greenlet \  
&& pip install \--install-option="--install-purelib=$PYTHONLIBPATH" eventlet \  
&& apt-get clean \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
\  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
EXPOSE 8080  
EXPOSE 5555  
EXPOSE 8793  
  
ADD script/entrypoint.sh /root/entrypoint.sh  
RUN chmod +x /root/entrypoint.sh  
ENTRYPOINT ["/root/entrypoint.sh"]  

