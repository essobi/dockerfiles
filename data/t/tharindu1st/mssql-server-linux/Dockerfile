FROM ubuntu:16.04  
ADD sqlservr.sh /  
RUN apt-get update  
RUN apt-get install -y curl libunwind8 libnuma1 libjemalloc1 libc++1 gdb
libcurl3 openssl python python3 libgssapi-krb5-2 wget apt-transport-https
locales software-properties-common python-software-properties  
  
RUN add-apt-repository "$(curl
https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2017.list)"  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee
/etc/apt/sources.list.d/msprod.list  
RUN apt-get update  
RUN apt-get install -y mssql-server mssql-server-fts  
RUN ACCEPT_EULA=y DEBIAN_FRONTEND=noninteractive MSSQL_PID=Developer \  
apt-get install -y --no-install-recommends mssql-tools unixodbc-dev  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc  
# Default SQL Server TCP/Port.  
EXPOSE 1433  
RUN locale-gen en_US.utf8 && update-locale  
ADD entrypoint.sh /  
CMD /entrypoint.sh  

