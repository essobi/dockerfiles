############################################################  
# Dockerfile to run dicom receive convert pipeline  
# Based on UBUNTU image  
############################################################  
  
FROM ubuntu:latest  
MAINTAINER korfiatisp@gmail.com  
  
  
# Setup a minimal env  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
  
# set a better shell prompt  
RUN echo 'export PS1="[\u@docker] \W # "' >> .bashrc  
  
  
# Install dependecies  
RUN apt-get update && apt-get install -y openssh-server apache2 supervisor  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
RUN apt-get install -y dcmtk  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN \  
apt-get update && \  
apt-get install -y python python-dev  
RUN apt-get install -y python-setuptools  
RUN easy_install pip  
RUN pip install numpy  
RUN apt-get install -y mricron  
RUN apt-get install -y net-tools  
RUN pip install python-dateutil --upgrade  
RUN pip install flask  
RUN pip install Werkzeug  
RUN apt-get install -y imagemagick  
# set root passord at image launch with -e ROOT_PASSWORD=my_secure_password  
ADD bootstrap.sh /usr/local/bin/bootstrap.sh  
  
COPY QIN /usr/local/lib/python2.7/dist-packages/QIN  
COPY tactic_client_lib /usr/local/lib/python2.7/dist-
packages/tactic_client_lib  
COPY ingest.config ./  
COPY ingest.py ./  
COPY main.sh ./  
COPY upload.py ./  
COPY radioreceiver.sh ./  
RUN chmod +x ingest.py  
RUN chmod +x main.sh  
RUN chmod +x radioreceiver.sh  
RUN chmod +x upload.py  
  
RUN mkdir DICOM  
# to correct --> TERM environment variable not set  
ENV TERM dumb  
# Start Tactic stack  
RUN echo 'export PS1="[\u@docker] \W # "' >> .bashrc  
USER root  
CMD ["./radioreceiver.sh"]  
EXPOSE 80 22 8832 5000  

