FROM openjdk:8-jre  
MAINTAINER Tilo Werner tilo.werner@moosbee.de  
  
ENV DEBIAN_FRONTEND="noninteractive"  
ARG user=mc  
ARG uid=6000  
ARG home=/opt/mc  
ARG port=25000  
ENV SERVER_VERSION="1.12.2"  
ENV SERVER_PORT=${port}  
ENV SERVER_USER=${user}  
  
ENV JAVA_OPTS="-Xmx1024M -Xms1024M"  
RUN apt-get update && apt-get --yes --no-install-recommends install wget git
vim && rm -rf /var/lib/apt/lists/*  
RUN useradd --uid ${uid} \--create-home --home-dir ${home} \--user-group
${user}  
  
VOLUME ${home}  
EXPOSE ${port}  
USER ${user}  
  
COPY entrypoint.sh entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

