FROM java:8  
  
RUN mkdir -p /data  
RUN wget \--progress=bar
"https://dma.ci.cloudbees.com/job/AisCoverage/lastSuccessfulBuild/artifact/target/*zip*/target.zip"
-O /archive.zip  
RUN unzip /archive.zip -d /  
ADD ./start.sh /start.sh  
  
EXPOSE 8090  
  
ENV SOURCE_NAME DEFAULT_SOURCE  
ENV CONFIG /data/default.xml  
  
CMD ["/bin/bash", "/start.sh"]  

