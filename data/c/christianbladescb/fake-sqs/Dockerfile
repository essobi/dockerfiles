FROM alpine:3.1  
MAINTAINER Christian Blades <christian.blades@careerbuilder.com>  
  
RUN apk -U add ruby ca-certificates && gem install --no-rdoc --no-ri fake_sqs  
  
EXPOSE 4567  
VOLUME ["/db"]  
  
ENTRYPOINT ["fake_sqs", "--port", "4567", "--bind", "0.0.0.0", "--database",
"/db/database.yml"]  

