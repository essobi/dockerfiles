FROM mesosphere/mesos-slave:1.1.1  
MAINTAINER Patrick Kleindienst <patrick.kleindienst@web.de>  
  
ARG AURORA_VERSION=0.17.0  
ENV USER=aurora  
ENV HOME=/home/aurora  
  
RUN apt-get update && \  
apt-get install -y python2.7 wget libcurl4-nss-dev  
  
RUN wget -c https://apache.bintray.com/aurora/ubuntu-trusty/aurora-
executor_${AURORA_VERSION}_amd64.deb && \  
dpkg -i aurora-executor_${AURORA_VERSION}_amd64.deb  
  
RUN useradd $USER \--create-home --shell /bin/bash && \  
usermod -aG docker $USER  
  
COPY thermos.sh /home/$USER/thermos.sh  
  
RUN chown $USER:$USER /home/$USER/thermos.sh && \  
chmod 500 /home/$USER/thermos.sh  
  
WORKDIR /home/$USER  
  
ENTRYPOINT ["./thermos.sh"]  

