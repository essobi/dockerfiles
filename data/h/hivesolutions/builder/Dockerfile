FROM hivesolutions/alpine_dev:latest  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
VOLUME /repo  
  
USER root  
  
ENV NAME ""  
ENV EXEC "/"  
ENV BUILDER "Dockerfile"  
ENV REPO "docker.stage.hive.pt"  
ADD run.sh /run.sh  
  
WORKDIR /repo  
  
RUN apk update && apk add docker  
  
CMD ["/run.sh"]  

