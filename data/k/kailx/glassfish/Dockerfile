FROM openjdk:6-slim  
MAINTAINER kailx  
  
ENV
GLASSFISH_DOWNLOAD_URL=http://download.oracle.com/glassfish/3.1.2.2/release/glassfish-3.1.2.2.zip  
  
WORKDIR /root  
RUN apt-get update && apt-get install -y wget procps python  
RUN wget ${GLASSFISH_DOWNLOAD_URL}  
RUN unzip glassfish-3.1.2.2.zip  
  
ENV GLASSFISH_ROOT=/root/glassfish3/glassfish  
  
COPY ./docker-entrypoint.d/* /docker-entrypoint.d/  
ENTRYPOINT ["python", "/docker-entrypoint.d/docker-entrypoint.py"]  

