FROM fumihiro/maven  
MAINTAINER Fumihiro Kato <fumi@fumi.me>  
LABEL version="0.1.0"  
  
RUN mkdir -p /work /data  
WORKDIR /work  
COPY run.sh .  
RUN chmod +x run.sh  
RUN git clone -b develop-ja https://github.com/fumi/extraction-framework.git  
  
WORKDIR extraction-framework  
RUN mvn clean install  
  
WORKDIR core  
RUN ../run download-ontology  
# Disabled because the download-mappings process is often stuck  
#RUN ../run download-mappings  
#RUN ../run generate-settings  
WORKDIR ../dump  
COPY *.properties ./  
  
ENTRYPOINT ["/work/run.sh"]  
CMD ["--help"]  

