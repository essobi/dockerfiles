FROM stlhrt/jdk8  
MAINTAINER Lukasz Wozniak  
  
# install serf  
USER root  
RUN apt-get update  
RUN apt-get install -qy unzip supervisor  
RUN mkdir -p /tmp/serf  
WORKDIR /tmp/serf  
ADD https://dl.bintray.com/mitchellh/serf/0.6.3_linux_amd64.zip
/tmp/serf/serf.zip  
RUN unzip serf.zip  
RUN mv serf /usr/bin/  
RUN rm -rf /tmp/serf  
  
# configure serf  
RUN mkdir -p /opt/serf/conf  
RUN mkdir -p /opt/serf/logs  
WORKDIR /opt/serf  
ADD serf-join.sh /opt/serf/serf-join.sh  
ADD supervisord-serf.conf /etc/supervisor/conf.d/supervisord-serf.conf  
RUN chmod 755 /opt/serf/*.sh  
  
#configure application launching  
ADD supervisord-app.conf /etc/supervisor/conf.d/supervisord-app.conf  
  
# Expose volume for additional serf config in JSON  
VOLUME /opt/serf/conf  
  
ENV APP_CMD /bin/bash -c 'while true; do echo "Nothing..."; sleep 5; done'  
CMD ["supervisord", "-n"]

