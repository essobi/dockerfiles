FROM frapontillo/java:8  
MAINTAINER Francesco Pontillo <francescopontillo@gmail.com>  
  
RUN apt-get update -y && apt-get install -y \  
wget  
RUN cd /opt/ \  
&& mkdir Youtrack  
  
WORKDIR /opt/Youtrack/  
RUN wget http://download-cf.jetbrains.com/charisma/youtrack-6.5.16367.jar  
  
ENV YOUTRACK_BASE_URL http://0.0.0.0  
ENV YOUTRACK_HOME_DIR /opt/Youtrack  
ENV YOUTRACK_DATA_DIR /opt/Youtrack/data  
ENV YOUTRACK_BACKUPS_DIR /opt/Youtrack/backups  
  
COPY run.sh /opt/Youtrack/  
RUN chmod +x run.sh  
  
EXPOSE 8080  
CMD []  
ENTRYPOINT ["/opt/Youtrack/run.sh"]

