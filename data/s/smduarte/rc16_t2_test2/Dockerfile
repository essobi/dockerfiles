FROM openjdk:8-jre  
  
MAINTAINER Sérgio Duarte (smd@fct.unl.pt)  
  
ENV HOME /root  
  
COPY media/* /movies/moana/  
COPY server/* /root/  
  
# Define working directory.  
WORKDIR /root  
  
EXPOSE 8080  
ENTRYPOINT ["java"]  
  
# Define default command.  
CMD ["-jar", "/root/pygmy-httpd-trab2.jar"]  

