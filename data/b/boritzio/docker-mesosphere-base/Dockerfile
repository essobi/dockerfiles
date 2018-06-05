FROM boritzio/docker-base-java  
  
RUN echo "deb http://repos.mesosphere.com/ubuntu/ trusty main" >
/etc/apt/sources.list.d/mesosphere.list >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF  
  
RUN apt-get update; apt-get install -y mesos=1.1.0-2.0.107.ubuntu1404  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

