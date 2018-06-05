FROM java:8  
RUN mkdir -p /data  
RUN wget --progress=bar
"https://dma.ci.cloudbees.com/job/AisView/lastSuccessfulBuild/artifact/*zip*/archive.zip"
-O /archive.zip  
RUN unzip /archive.zip -d /  
RUN mkdir -p /aisview-backup  
ADD ./start.sh /start.sh  
EXPOSE 8090  
ENV BACKUP /aisview-backup  
CMD ["/bin/bash", "/start.sh"]  

