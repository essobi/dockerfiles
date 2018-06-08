FROM ruby:alpine  
  
LABEL maintainer="Sherpany DevOps Team <devops@sherpany.com>"  
  
WORKDIR /app  
  
RUN apk add \--update ruby && \  
apk upgrade && \  
apk add \--virtual build-deps build-base && \  
gem install sass && \  
apk del build-deps && \  
rm -rf /var/cache/apk  
  
ENTRYPOINT ["sass"]  

