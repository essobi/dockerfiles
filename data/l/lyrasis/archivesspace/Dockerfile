FROM lyrasis/archivesspace:base  
MAINTAINER Mark Cooper <mark.c.cooper@outlook.com>  
  
ENV
ARCHIVESSPACE_REPOSITORY=https://github.com/archivesspace/archivesspace.git \  
ASPACE_PUBLIC_DEV=false \  
ARCHIVESSPACE_DB_TYPE=demo \  
ARCHIVESSPACE_DB_HOST_TYPE=internal \  
ARCHIVESSPACE_DB_NAME=archivesspace \  
ARCHIVESSPACE_DB_USER=archivesspace \  
ARCHIVESSPACE_DB_PASS=archivesspace  
  
RUN wget http://central.maven.org/maven2/mysql/mysql-connector-
java/5.1.39/mysql-connector-java-5.1.39.jar  
  
RUN mkdir -p /source  
RUN git clone $ARCHIVESSPACE_REPOSITORY /source/archivesspace  
  
# PROCESS BUILD  
WORKDIR /source/archivesspace  
RUN ./scripts/build_release -t  
RUN mv ./*.zip /  
RUN rm -rf /source  
  
# UNPACK BUILD  
WORKDIR /  
RUN unzip /*.zip -d /  
RUN rm /*.zip  
RUN rm -rf /archivesspace/plugins/*  
RUN chmod 755 /archivesspace/archivesspace.sh  
  
# FINALIZE SETUP  
RUN cp /mysql-connector-java-5.1.39.jar /archivesspace/lib/  
ADD setup.sh /setup.sh  
RUN chmod u+x /*.sh  
  
EXPOSE 8080 8081 8089 8090  
CMD ["/setup.sh"]

