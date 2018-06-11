FROM nlescstoryteller/storyteller  
  
VOLUME /data  
  
COPY . /src/query-builder-xenon  
  
WORKDIR /src/query-builder-xenon/bin/  
RUN chmod +x xenon-flow  
  
WORKDIR /src/query-builder-xenon/cwl/  
# RUN wget KNOWLEDGE_STORE_SERVER_URL/token.index.gz  
RUN chmod +rx *  
  
WORKDIR /src/query-builder-xenon  
  
EXPOSE 4567  
CMD ["./bin/xenon-flow"]  

