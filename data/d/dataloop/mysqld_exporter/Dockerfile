FROM dataloop/agent-base:latest  
MAINTAINER Tom Ashley <tom@dataloop.io>  
  
  
RUN curl -L -k
https://github.com/prometheus/mysqld_exporter/releases/download/0.8.1/mysqld_exporter-0.8.1.linux-
amd64.tar.gz -o /mysqld_exporter-0.8.1.linux-amd64.tar.gz  
RUN tar -xvzf /mysqld_exporter-0.8.1.linux-amd64.tar.gz  
RUN mv mysqld_exporter-0.8.1.linux-amd64/mysqld_exporter /bin  
  
ADD root /  
  
EXPOSE 9104  

