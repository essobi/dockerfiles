FROM delitescere/jdk:8  
MAINTAINER Rajat Vig <rajat.vig@gmail.com>  
  
ENV DATADIR /var/lib/dynamo  
  
USER root  
  
RUN addgroup -g 9999 docker && \  
adduser -u 9999 -G docker -D -g "Docker User" docker  
  
RUN mkdir $DATADIR && chown docker:docker $DATADIR  
USER docker  
  
WORKDIR /home/docker  
  
RUN wget -O /home/docker/dynamodb_local_latest.tar.gz http://dynamodb-
local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest && \  
tar xzf /home/docker/dynamodb_local_latest.tar.gz && \  
rm /home/docker/dynamodb_local_latest.tar.gz  
  
EXPOSE 8000  
VOLUME $DATADIR  
  
COPY cmd.sh /home/docker/cmd.sh  
  
CMD ["/home/docker/cmd.sh", "-dbPath /var/lib/dynamo"]  

