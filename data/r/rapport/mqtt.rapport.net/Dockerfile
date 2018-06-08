FROM ubuntu:latest  
MAINTAINER Gary Cornelius <gary.cornelius@rapport.net>  
  
#
--------------------------------------------------------------------------------  
# Linux environment  
#
--------------------------------------------------------------------------------  
ENV DEBIAN_FRONTEND noninteractive  
ENV MOSQUITTO_VERSION 1.4.2  
RUN apt-get update && apt-get install -y  
RUN apt-get install wget build-essential libwrap0-dev libssl-dev python-
distutils-extra libc-ares-dev uuid-dev -y  
  
# create user to start deamnon  
RUN adduser --system --disabled-password --disabled-login mosquitto  
RUN groupadd -r mqtt && adduser --system --disabled-password --disabled-login
mqtt  
  
# install mosquitto into mqt users home directory which as appropriate
permissions  
RUN cd /home/mqtt/ && wget
http://mosquitto.org/files/source/mosquitto-${MOSQUITTO_VERSION}.tar.gz  
RUN cd /home/mqtt/ && tar zxvf mosquitto-${MOSQUITTO_VERSION}.tar.gz  
RUN cd /home/mqtt/mosquitto-${MOSQUITTO_VERSION} && make all  
RUN cd /home/mqtt/mosquitto-${MOSQUITTO_VERSION} && make install  
RUN ldconfig  
  
# /home/mqtt/mosquitto-1.4.2/mosquitto.conf  
# /home/mqtt/mosquitto-${MOSQUITTO_VERSION}/mosquitto.conf  
# volume share 256 300  
# /home/mqtt/mqttwarn > /ecs/mqttwarn mqttwarn.ini | samplefuncs.py  
# /usr/local/etc > /ecs/etc mqttcollect.ini  
# /etc/collectd > /ecs/collectd  
#
--------------------------------------------------------------------------------  
# Collectd  
# Logs: /var/log/collectd.log  
#
--------------------------------------------------------------------------------  
# should use install from ubuntu container??  
RUN apt-get --yes install collectd-core collectd-dev  
  
# volume share  
ADD conf/collectd.conf /etc/collectd/collectd.conf  
RUN chmod 777 /etc/collectd/collectd.conf  
  
#
--------------------------------------------------------------------------------  
# MQTTCOLLECT: http://supervisord.org/  
#
--------------------------------------------------------------------------------  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install software-properties-common python-software-properties  
  
RUN apt-add-repository ppa:mosquitto-dev/mosquitto-ppa  
RUN apt-get update  
RUN apt-get install -y libmosquitto-dev  
RUN apt-get install -y git  
RUN cd /home/mqtt/ && git clone https://github.com/jpmens/mqttcollect  
RUN cd /home/mqtt/mqttcollect && make  
  
ADD conf/mqttcollect.ini /usr/local/etc/  
RUN chmod 777 /usr/local/etc/mqttcollect.ini  
  
#
--------------------------------------------------------------------------------  
# MQTTWARN: http://supervisord.org/  
#
--------------------------------------------------------------------------------  
# RUN apt-get install -y python3-dev  
RUN apt-get install -y libffi-dev  
RUN apt-get install -y libssl-dev  
RUN cat /tmp/get-pip.py | python3  
RUN apt-get install python-pip --yes --force-yes  
RUN pip install paho-mqtt slacker  
  
RUN cd /home/mqtt && git clone https://github.com/jpmens/mqttwarn.git  
  
# Add configuration files in volume share  
ADD conf/mqttwarn.ini /home/mqtt/mqttwarn/mqttwarn.ini  
RUN chmod 777 /home/mqtt/mqttwarn/mqttwarn.ini  
ADD conf/samplefuncs.py /home/mqtt/mqttwarn/samplefuncs.py  
RUN chmod 777 /home/mqtt/mqttwarn/samplefuncs.py  
  
#
--------------------------------------------------------------------------------  
# Supervisor: http://supervisord.org/  
#
--------------------------------------------------------------------------------  
# STEP 1: Download software, install and tidy up  
RUN apt-get update \  
&& apt-get install -y supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
# STEP 2: Configuration  
RUN echo '[supervisord]\nnodaemon=true\n\n' >
/etc/supervisor/conf.d/supervisord.conf  
  
# Mosquitto process  
RUN echo '[program:mosquitto]\nuser=mqtt\ncommand=/usr/local/sbin/mosquitto -d
-c /home/mqtt/mosquitto-1.4.2/mosquitto.conf\nstdout_logfile =
/var/log/supervisor/%(program_name)s.log\nstderr_logfile =
/var/log/supervisor/%(program_name)s.log\nautorestart = true\n\n' >>
/etc/supervisor/conf.d/supervisord.conf  
  
# MQTTwarn process  
RUN echo
'[program:mqttwarn]\ndirectory=/home/mqtt/mqttwarn\nuser=mqtt\ncommand=python
/home/mqtt/mqttwarn/mqttwarn.py\nstdout_logfile =
/var/log/supervisor/%(program_name)s.log\nstderr_logfile =
/var/log/supervisor/%(program_name)s.log\nautorestart = true\n\n' >>
/etc/supervisor/conf.d/supervisord.conf  
  
#
--------------------------------------------------------------------------------  
# Docker: https://www.docker.com/  
#
--------------------------------------------------------------------------------  
# Expose Ports  
EXPOSE 1883  
CMD ["/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/conf.d/supervisord.conf"]  

