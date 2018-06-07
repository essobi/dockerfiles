FROM ubuntu  
MAINTAINER lambda_sakura  
RUN apt-get install -y curl  
RUN mkdir /cim  
ENV CIM_HOME /cim  
RUN curl -L https://raw.github.com/KeenS/CIM/master/scripts/cim_installer |
CIM_HOME=/cim/ /bin/sh  
RUN echo ". '/cim/init.sh'" >> /root/.bashrc  
  

