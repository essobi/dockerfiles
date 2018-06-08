FROM microsoft/mssql-server-linux:2017-CU3  
  
ENV ACCEPT_EULA=Y  
ENV SA_PASSWORD=Softwareplant123  
  
RUN locale-gen en_US.utf8 && update-locale  
  
RUN apt-get update && apt-get install -y curl apt-transport-https  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee
/etc/apt/sources.list.d/msprod.list  
  
RUN apt-get update && apt-get install -y mssql-tools gettext  
  
ADD init-j7.sh /  
ADD docker-entrypoint.sh /  
ADD jira7.bak /  
RUN chmod a+x docker-entrypoint.sh init-j7.sh  
  
ENTRYPOINT /docker-entrypoint.sh  

