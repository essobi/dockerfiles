FROM openjdk:8-jdk  
  
MAINTAINER Luis David Barrios Alfonso (luisdavid.barrios@agsnasoft.com /
cyberluisda@gmail.com)  
  
ADD files/java-launch.sh /bin/  
RUN chmod a+x /bin/java-launch.sh  
  
VOLUME /usr/lib/java/extra  
  
ENV CLASSPATH /usr/lib/java/extra/*  
  
ENTRYPOINT ["/bin/java-launch.sh"]  
CMD ["--help"]  

