# docker build -t fiware-glancesync --no-cache=true --pull=true .  
FROM centos  
RUN yum install -y epel-release  
RUN yum update -y  
RUN yum install -y crudini gcc libffi-devel openssl-devel git gcc build-
essentials python-devel python-pip  
RUN mkdir /opt/fiware; mkdir /etc/fiware.d/; mkdir /etc/fiware.d/etc/  
ENV GLANCESYNC_SETTINGS_FILE=/etc/fiware.d/etc/fiware-glancesync.cfg  
ENV GLANCESYNC_LOGGING_SETTINGS_FILE=/etc/fiware.d/etc/fiware-glancesync-
logging.cfg  
COPY fiware-glancesync.cfg /etc/fiware.d/etc/fiware-glancesync.cfg  
COPY fiware-glancesync-logging.cfg /etc/fiware.d/etc/fiware-glancesync-
logging.cfg  
COPY glancesync.conf /etc/glancesync.conf  
RUN pip install --upgrade pip  
RUN pip install git+https://github.com/telefonicaid/fiware-glancesync@develop  
EXPOSE 8080  
COPY start.sh start.sh  
RUN mkdir /var/lib/glance  
CMD ./start.sh  
  

