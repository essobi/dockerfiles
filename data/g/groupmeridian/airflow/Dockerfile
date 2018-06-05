  
# airflow  
FROM centos/python-35-centos7  
  
MAINTAINER Matthew Brown <matthew.brown@meridianholdings.co.za>  
  
ENV AIRFLOW_VERSION=1.8.1  
ENV AIRFLOW_HOME=/opt/app-root  
ENV BUILDER_VERSION 1.0  
LABEL io.k8s.description="Apache Airflow is a flexible scheduling and ETL
tool" \  
io.k8s.display-name="apache airflow 1.8.1" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="apache airflow,1.8.1"  
  
RUN /bin/bash -c "pip install pytz pyOpenSSL ndg-httpsclient pyasn1 \  
apache-airflow[crypto,postgres,hive,hdfs,jdbc,password]==${AIRFLOW_VERSION}"  
  
# TODO (optional): Copy the builder files into /opt/app-root  
# COPY ./<builder_folder>/ /opt/app-root/  
# TODO: Copy the S2I scripts to /usr/libexec/s2i, since openshift/base-centos7
image  
# sets io.openshift.s2i.scripts-url label that way, or update that label  
COPY ./s2i/bin/ /usr/libexec/s2i  
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg  
  
#RUN chown -R 1001:1001 $AIRFLOW_HOME  
# This default user is created in the openshift/base-centos7 image  
USER 1001  
EXPOSE 8080  
CMD ["/usr/libexec/s2i/run"]  

