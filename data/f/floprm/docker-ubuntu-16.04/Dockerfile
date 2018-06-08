FROM ubuntu:xenial  
MAINTAINER Floprm "https://github.com/FPRM"  
ENV export DEBIAN_FRONTEND=noninteractive  
  
# compilers and basic tools  
RUN apt-get update && apt-get install -y \  
tzdata \  
locales  
  
RUN ln -fs /usr/share/zoneinfo/EUROPE/Paris /etc/localtime  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
RUN sed -i -e 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8/' /etc/locale.gen && \  
locale-gen  
  
RUN echo $date +”%Z %z”  
RUN echo /etc/locale.conf

