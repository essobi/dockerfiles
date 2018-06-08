FROM foxylion/jenkins  
MAINTAINER Mishel Uchuari <dmuv7@hotmail.com>  
  
RUN /usr/local/bin/install-plugins.sh workflow-remote-loader workflow-
aggregator build-pipeline-plugin  
#Se fija un usuario y una contrasena para ejecutar jenkins  
ENV JENKINS_USER replicate  
ENV JENKINS_PASS replicate  
ENV JENKINS_OPTS \--prefix=/jenkins  
  
#Instalaciones  
USER root  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get install -y apt-utils  
RUN apt-get install -y python-pip  
RUN apt install -y linuxbrew-wrapper  
  
#Instalaciones jenkins job builder plugin  
RUN pip install jenkins-job-builder==2.0.0.0b2  
RUN pip install PyYAML python-jenkins  
  
#Se cambia la configuracion del archivo executors.groovy  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/  
  
#Se usa el plugin para crear el pipeline in Jenkins  
RUN mkdir /etc/jenkins_jobs/  
ADD jenkins_jobs.ini /etc/jenkins_jobs/  
ADD scm_pipeline.yaml /etc/jenkins_jobs/  
ADD script-to-execute.sh /etc/jenkins_jobs/  

