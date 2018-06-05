FROM ubuntu:xenial  
MAINTAINER Cyle Riggs <beardedfoo@gmail.com>  
  
# Add the mssql repos  
RUN apt-get update  
RUN apt-get -y install apt-transport-https curl  
COPY microsoft.asc /tmp/microsoft.asc  
RUN apt-key add /tmp/microsoft.asc  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee
/etc/apt/sources.list.d/msprod.list  
RUN apt-get update  
  
# Setup the locale  
RUN apt-get -y install locales  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
# Install mssql-tools  
ENV ACCEPT_EULA=Y  
RUN apt-get -y install mssql-tools unixodbc-dev  
ENV PATH="/opt/mssql-tools/bin/:${PATH}"  

