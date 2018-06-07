FROM buildpack-deps:curl AS download-env  
RUN wget https://raw.githubusercontent.com/mongodb/docs-assets/primer-
dataset/primer-dataset.json  
  
FROM mongo:latest AS runtime-env  
ENV MONGO_SERVER= MONGO_PORT=27017 MONGO_DATABASE=test  
COPY \--from=download-env primer-dataset.json .  
ADD sample-entrypoint.sh /examples/sample-entrypoint.sh  
ENTRYPOINT ["/examples/sample-entrypoint.sh"]  

