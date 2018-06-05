FROM ruby:latest  
RUN gem install apiaryio  
RUN touch /tmp/api.apib  
ARG APIB_PATH="api.apib"  
ENV APIB_PATH $APIB_PATH  
VOLUME /tmp  
EXPOSE 8080  
ENTRYPOINT ["/bin/bash", "-c", "apiary preview --path=/tmp/$APIB_PATH \--watch
--server --host=0.0.0.0"]  

