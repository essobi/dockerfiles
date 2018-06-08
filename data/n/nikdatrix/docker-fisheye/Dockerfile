FROM nikdatrix/docker-base:ubuntu  
  
MAINTAINER Felipe Restrepo, felipe.restrepo@allegorithmic.com  
  
# Enviroment  
ENV FISHEYE_VERSION 4.2.0  
ENV FISHEYE_INST /opt/fisheye/fecru-${FISHEYE_VERSION}  
ENV FISHEYE_HOME /var/atlassian/fisheye  
ENV MYSQL_CONNECTOR_VERSION 5.1.39  
ENV WORKDIR /opt/fisheye  
  
# add some basic scripts  
# ADD helper.sh /usr/local/share/fisheye/helper.sh  
RUN echo "Atlassian - FishEye ${FISHEYE_VERSION} applications runtime
environment"  
  
# Workdir  
WORKDIR $WORKDIR  
RUN mkdir -p $WORKDIR  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install \  
\--no-install-recommends -y -qq \  
curl unzip openjdk-8-jdk  
  
RUN apt-get clean \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /etc/ssh/ssh_host_*  
  
# Volumes  
VOLUME ["$FISHEYE_INST"]  
VOLUME ["$FISHEYE_HOME"]  
  
# Entrypoint  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8060  
CMD ["bin/fisheyectl.sh", "run"]  

