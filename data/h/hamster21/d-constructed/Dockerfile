FROM ubuntu:13.10  
MAINTAINER Hans Meyer, hamster.of.dev@gmail.com  
RUN apt-get update -y  
RUN apt-get install -y wget gcc-multilib xdg-utils libcurl4-openssl-dev  
RUN wget -q http://downloads.dlang.org/releases/2013/dmd_2.064.2-0_amd64.deb  
RUN dpkg -i dmd_2.064.2-0_amd64.deb

