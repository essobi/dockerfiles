FROM solr  
  
MAINTAINER Allen Day "allenday@allenday.com"  
USER root  
WORKDIR /  
  
ENV BUILD_PACKAGES=""  
ENV IMAGE_PACKAGES="git maven telnet openjdk-8-jdk"  
RUN apt-get -y update  
RUN apt-get -y --no-install-recommends install $BUILD_PACKAGES $IMAGE_PACKAGES  
  
#tomcat http  
EXPOSE 9999  
#solr http  
EXPOSE 8983  
## cleanup  
#RUN apt-get -y remove --purge $BUILD_PACKAGES  
#RUN apt-get -y remove --purge $(apt-mark showauto)  
#RUN rm -rf /var/lib/apt/lists/*  
RUN git clone https://github.com/allenday/image-similarity.git  
RUN cd image-similarity && mvn install assembly:single -DskipTests  
  
COPY entrypoint.sh /entrypoint.sh  
COPY uploadservlet /uploadservlet  
RUN cd /uploadservlet && mvn package  
  
USER solr  
WORKDIR /tmp  
  
RUN solr start && sleep 5 && solr create_core -c frameshift -p 8983 && solr
stop -p 8983  
COPY managed-schema /opt/solr/server/solr/frameshift/conf/managed-schema  
  
ENTRYPOINT ["/bin/bash","/entrypoint.sh"]  
  

