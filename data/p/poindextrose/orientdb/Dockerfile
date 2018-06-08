# orientdb  
#  
# VERSION: see `TAG`  
FROM joaodubas/openjdk:latest  
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"  
# install system deps  
RUN apt-get -y -qq update \  
&& apt-get -y -qq install curl  
  
# install orientdb  
ENV ROOT /opt/orientdb  
ENV ORIENT_VERSION orientdb-community-2.0.7  
ENV ORIENT_URL
http://www.orientechnologies.com/download.php?email=unknown@unknown.com&file=${ORIENT_VERSION}.tar.gz&os=linux  
RUN mkdir ${ROOT}  
RUN cd ${ROOT}  
RUN curl ${ORIENT_URL} > ${ORIENT_VERSION}.tar.gz  
RUN tar -xzf ${ORIENT_VERSION}.tar.gz -C /opt/orientdb --strip-components=1  
RUN rm ${ORIENT_VERSION}.tar.gz  
RUN ln -s ${ROOT}/bin/* /usr/local/bin/  
RUN mkdir /usr/local/log  
  
# cleanup  
RUN apt-get -y -qq --force-yes clean \  
&& rm -rf /opt/downloads/linux /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# configure system  
EXPOSE 2424  
EXPOSE 2480  
CMD ["/usr/local/bin/server.sh"]  

