FROM python:3.6.4-alpine3.7  
RUN apk update && apk upgrade && \  
apk add \--no-cache $RUBY_PACKAGES && \  
apk add \--no-cache --virtual build-deps $BUILD_PACKAGES && \  
apk del build-deps  
RUN pip install rq-dashboard==0.3.10  
EXPOSE 9181  
ENTRYPOINT ["rq-dashboard"]  

