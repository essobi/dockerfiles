FROM praekeltfoundation/python3-base:debian  
MAINTAINER Picsa <engineering@picsa.com>  
  
# Airflow  
ARG AIRFLOW_VERSION=1.7.1.3  
ENV AIRFLOW_HOME /airflow_home  
  
  
# Install airflow and deps  
RUN set -ex \  
&& useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \  
&& apt-get-install.sh build-essential \  
&& pip install celery==3.1.23 \  
&& pip install amqp==2.1.4 \  
&& pip install airflow[celery,postgres,s3,password,hdfs]==$AIRFLOW_VERSION \  
&& apt-get-purge.sh build-essential  
  
EXPOSE 8080 5555 8793  
RUN chown -R airflow:airflow ${AIRFLOW_HOME}  
  
COPY script/entrypoint.sh /entrypoint.sh  
WORKDIR ${AIRFLOW_HOME}  
ENTRYPOINT ["/entrypoint.sh"]  
  
ONBUILD ADD airflow_home ${AIRFLOW_HOME}/  
# chown the app directory after copying in case the copied files include  
# subdirectories that will be written to, e.g. the media directory  
ONBUILD RUN chown -R airflow:airflow ${AIRFLOW_HOME}  
ONBUILD USER airflow  

