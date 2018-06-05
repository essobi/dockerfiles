FROM ubuntu:trusty  
MAINTAINER bem@hq.realgeeks.com  
  
RUN apt-get update && \  
apt-get install -y git python python-dev python-pip openssl gfortran make gcc
build-essential libffi-dev libssl-dev pkg-config libfreetype6-dev libpng-dev
&& \  
rm -rf /var/lib/apt/lists/*  
  
ENV WORKDIR /tmp  
WORKDIR ${WORKDIR}  
COPY requirements.txt ${WORKDIR}/  
RUN pip install -r ${WORKDIR}/requirements.txt  

