FROM ubuntu:14.04.1  
MAINTAINER Lukasz Wozniak  
  
# get dependencies  
RUN apt-get update -q  
RUN apt-get upgrade -qy  
RUN apt-get install -qy build-essential git supervisor unzip  
  
# get serf  
RUN mkdir -p /tmp/serf  
WORKDIR /tmp/serf  
ADD https://dl.bintray.com/mitchellh/serf/0.6.3_linux_amd64.zip
/tmp/serf/serf.zip  
RUN unzip serf.zip  
RUN mv serf /usr/bin/  
RUN rm -rf /tmp/serf  
  
# configure non root user to run  
RUN useradd -m service  
  
# configure serf  
RUN mkdir -p /opt/serf/conf  
RUN mkdir -p /opt/serf/logs  
WORKDIR /opt/serf  
ADD /supervisord-serf.conf /etc/supervisor/conf.d/supervisord-serf.conf  
ADD /50-defaults.json /opt/serf/conf/50-defaults.json  
RUN chown -R service:service /opt  
  
# Cleanup test  
RUN apt-get -qq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Expose volume for additional serf config in JSON  
VOLUME /opt/serf/conf  
VOLUME /opt/serf/logs  
  
EXPOSE 7946 7373  
CMD ["supervisord", "-n"]

