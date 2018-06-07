FROM ruby:2.0-onbuild  
ENV META_PATH=meta.json  
ENV SCHEMATA_PATH=schemata/  
ENV SCHEMA_PATH=schema.json  
  
CMD sh -c 'prmd combine --meta $META_PATH $SCHEMATA_PATH > $SCHEMA_PATH &&
prmd verify $SCHEMA_PATH > /dev/null'  

