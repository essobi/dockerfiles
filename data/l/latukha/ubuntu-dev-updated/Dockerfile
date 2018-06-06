FROM ubuntu:17.04  
MAINTAINER Anton Latukha <anton.latukha+docker@gmail.com>  
  
# Disabling ncurses package post-installation menus  
ENV DEBIAN_FRONTEND noninteractive  
  
# Tracking all changes, cleaning packages that become dangling on update  
RUN apt update \  
&& apt --yes upgrade \  
&& apt --yes autoclean \  
&& apt --yes autoremove  
  
# Caching layers  
RUN apt-get update  
RUN apt-get upgrade  

