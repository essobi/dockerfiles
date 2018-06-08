FROM ruby:2.1-onbuild  
RUN mkdir /dynamodb_table_defs  
VOLUME /dynamodb_table_defs  
  
RUN chmod a+x ./dynamo_build_config.rb  
  
CMD ["./dynamo_build_config.rb", "--config_file", "config.json"]  

