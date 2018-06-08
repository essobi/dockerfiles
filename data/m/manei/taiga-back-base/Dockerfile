FROM python:3.4-slim  
MAINTAINER Mihai Anei <mihai.anei@gmail.com>  
LABEL Description="Taiga Backend Base Image"  
  
RUN apt-get update && apt-get install -y build-essential binutils-doc autoconf
flex bison libjpeg-dev \  
&& apt-get install -y libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev
libncurses5-dev \  
&& apt-get install -y automake libtool libffi-dev curl git tmux gettext \  
&& apt-get install -y libxml2-dev libxslt-dev \  
&& apt-get install -y postgresql-server-dev-9.4  

