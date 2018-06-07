FROM ubuntu:16.04  
  
ENV ACCEPT_EULA Y  
  
RUN apt-get update && \  
apt-get install curl apt-transport-https locales unixodbc-dev -y && \  
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add \- && \  
curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee
/etc/apt/sources.list.d/msprod.list  
  
RUN locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8  
  
RUN apt-get update && \  
apt-get install mssql-tools -y && \  
apt-get remove \--purge curl apt-transport-https -y  
  
ENV PATH ${PATH}:/opt/mssql-tools/bin  
  
EXPOSE 1433  
  
CMD ["/bin/bash"]  

