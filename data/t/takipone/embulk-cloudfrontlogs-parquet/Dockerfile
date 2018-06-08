FROM takipone/embulk:latest  
  
RUN /embulk/embulk gem install embulk-input-s3 embulk-output-parquet  
  
COPY ./config.yml.liquid /config.yml.liquid  
  
CMD ["run", "/config.yml.liquid"]  

