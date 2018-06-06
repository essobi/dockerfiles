FROM takipone/embulk:latest  
  
RUN /embulk/embulk gem install embulk-input-s3 embulk-parser-jsonl embulk-
output-td  
  
COPY ./config.yml.liquid /config.yml.liquid  
  
CMD ["run", "/config.yml.liquid"]  

