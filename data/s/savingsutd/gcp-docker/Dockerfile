FROM google/cloud-sdk:167.0.0  
  
MAINTAINER Ain Tohvri <ain.tohvri@savings-united.com>  
  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get autoremove && \  
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O
$HOME/cloud_sql_proxy && \  
chmod +x $HOME/cloud_sql_proxy && \  
mkdir /cloudsql  

