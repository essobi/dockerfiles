FROM ubuntu:trusty  
MAINTAINER Vasanth KG <vasanth@egovernments.org>  
RUN apt-get update -y \  
&& apt-get install wget curl build-essential ntp fontconfig unzip -y \  
&& apt-get install -y maven git  
  
# Application PATH  
RUN mkdir -p /opt/lapp  
ENV HOME_PATH /opt/lapp  
#WORKDIR  
# Install Postgres  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo
apt-key add - \  
&& apt-get update && apt-get install postgresql-9.4 -y  
ENV PGPASSWORD postgres  
# Adjust PostgreSQL configuration so that remote connections  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.4/main/pg_hba.conf  
# And add ``listen_addresses`` to ``/etc/postgresql/9.4/main/postgresql.conf``  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf  
RUN /etc/init.d/postgresql restart && sudo -u postgres psql --command "alter
user postgres with password 'postgres';"  
  
# Install JDK  
RUN wget -O ${HOME_PATH}/jdk-8u66-linux-x64.tar.gz
http://devops.egovernments.org/downloads/jdk/jdk-8u66-linux-x64.tar.gz \  
&& tar -xvf ${HOME_PATH}/jdk-8u66-linux-x64.tar.gz -C ${HOME_PATH} \  
&& rm ${HOME_PATH}/jdk-8u66-linux-x64.tar.gz  
# Set JAVA_HOME  
ENV JAVA_HOME ${HOME_PATH}/jdk1.8.0_66  
  
# Install Redis  
RUN apt-get install redis-server -y  
  
# Install ES 1.7.4  
RUN wget -O ${HOME_PATH}/elasticsearch-1.7.1.tar.gz
http://devops.egovernments.org/downloads/es/elasticsearch-1.7.1.tar.gz \  
&& tar -xvf ${HOME_PATH}/elasticsearch-1.7.1.tar.gz -C ${HOME_PATH} \  
&& rm ${HOME_PATH}/elasticsearch-1.7.1.tar.gz  
  
#PORT expose local  
EXPOSE 5432 8080 9990 6379 9200 9300  
# Install WildFly  
RUN wget -O ${HOME_PATH}/wildfly-9.0.2.Final.zip
http://devops.egovernments.org/downloads/wildfly/wildfly-9.0.2.Final.zip \  
&& unzip ${HOME_PATH}/wildfly-9.0.2.Final.zip -d ${HOME_PATH} \  
&& rm ${HOME_PATH}/wildfly-9.0.2.Final.zip  
# Set the JBOSS_HOME env variable  
ENV WILDFLY_HOME ${HOME_PATH}/wildfly-9.0.2.Final  
#Add launcher script  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
# Entry point to start multiple services  
ENTRYPOINT [ "/run.sh", "/opt/lapp", "/opt/lapp/wildfly-9.0.2.Final" ]  
#CMD [ "/opt/lapp/wildfly-9.0.2.Final/bin/standalone.sh", "-b", "0.0.0.0",
"-bmanagement", "0.0.0.0" ]  

