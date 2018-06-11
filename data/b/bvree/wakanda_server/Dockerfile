FROM ubuntu:16.04  
MAINTAINER Bert Vree <XXXXXX@XXXX.nl>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV VERSION v2.3.0  
ENV PACKAGE wakanda-community-server_2.3.0_amd64.deb  
  
RUN apt-get update \  
&& apt-get install -y wget libcap-ng-utils \  
&& apt-get clean  
  
WORKDIR /tmp/  
  
RUN wget -qL https://github.com/Wakanda/wakanda-digital-app-
factory/releases/download/v2.3.0/wakanda-community-server_2.3.0_amd64.deb \  
&& dpkg -i wakanda-community-server_2.3.0_amd64.deb \  
&& rm wakanda-community-server_2.3.0_amd64.deb  
  
EXPOSE 8080 4433

