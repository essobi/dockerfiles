FROM huggosantos/jdk8  
  
USER root  
# Set the WILDFLY_VERSION env variable  
WORKDIR /opt/jboss  
  
ENV WILDFLY_VERSION 10.0.0.Final  
  
ENV DOWNLOAD_URL=http://download.jboss.org/wildfly/$WILDFLY_VERSION  
  
RUN wget ${DOWNLOAD_URL}/wildfly-$WILDFLY_VERSION.tar.gz  
RUN tar -xf wildfly-$WILDFLY_VERSION.tar.gz  
RUN rm wildfly-$WILDFLY_VERSION.tar.gz  
RUN ln -s wildfly-$WILDFLY_VERSION wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
# add management user (username: admin, passwd: wildfly)  
RUN /opt/jboss/wildfly/bin/add-user.sh admin wildfly --silent  
  
EXPOSE 8080 9990  
#CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  
# docker build --no-cache -t eunaifba/wildfly:9.0.2 .  
# docker run -d --name wildfly9 -p 8080:8080 -p 9990:9990
eunaifba/wildfly:9.0.2  
# docker exec -it wildfly9 bash  
# docker rmi eunaifba/wildfly:9.0.2  

