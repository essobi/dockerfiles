FROM tutum/apache-php  
  
MAINTAINER Samuel Wicky <samuel.wicky@avq.ch>  
  
RUN apt-get update -q && \  
apt-get install -y -q wget unzip php5-sqlite && \  
rm -rf /app/* && \  
wget -P /app https://github.com/ecleese/plexWatchWeb/archive/master.zip && \  
unzip /app/master.zip -d /app && \  
mv /app/plexWatchWeb-master/* /app && \  
rm -rf /app/master.zip plexWatchWeb-master  
  
COPY ./config.php /app/config/  
  
VOLUME /app  
VOLUME /data  

