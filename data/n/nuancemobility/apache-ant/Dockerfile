FROM java:8  
MAINTAINER Brice Argenson <brice.argenson@nuance.com>  
  
ENV ANT_VERSION 1.9.5  
RUN wget http://www.us.apache.org/dist//ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /opt/ant && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
  
VOLUME /project  
  
WORKDIR /project  
  
ENTRYPOINT [ "/opt/ant/bin/ant"]  
CMD [ "-help" ]

