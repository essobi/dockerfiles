# using the latest OpenJDK 8 update (see
https://registry.hub.docker.com/u/library/java/ for more details)  
FROM openjdk:8-jdk-alpine  
MAINTAINER Anthony Dahanne <anthony.dahanne@softwareag.com>  
  
# add few utilities, upgrade tar  
RUN apk --update add tar openssl ca-certificates bash curl git  
  
RUN mkdir /root/app  
WORKDIR /root/app/  
  
RUN echo "yup"  
  
RUN git clone https://github.com/anthonydahanne/spring-petclinic.git
/root/app/ \  
&& git checkout ehcache3-boot-clustered  
  
# in a more serious deployment scenario and environment, this is where you
would download your java jar  
RUN ./mvnw clean package \  
&& rm -rf /.m2/repository  
  
# add the clustered config  
ADD config/ /root/app/config/  
ENV SPRING_CACHE_JCACHE_CONFIG "file:///root/app/config/ehcache-clustered.xml"  
ENV OFFHEAP_RESOURCE_NAME "primary-server-resource"  
VOLUME /tmp  
EXPOSE 8080  
ENTRYPOINT sed -i -r 's/OFFHEAP_RESOURCE_NAME/'$OFFHEAP_RESOURCE_NAME'/'
/root/app/config/ehcache*.xml \  
&& cat /root/app/config/ehcache-clustered.xml \  
&& java -Djava.security.egd=file:/dev/./urandom -jar
/root/app/target/petclinic.war \  
  

