FROM alpine:3.7  
MAINTAINER Benoit Chabord <>  
  
RUN apk --no-cache add ca-certificates curl bash jq py-pip tar && pip install
awscli --no-cache-dir  
  
# add ecs-deploy  
# https://github.com/silinternational/ecs-deploy  
RUN mkdir tempfolder && \  
curl -L https://api.github.com/repos/silinternational/ecs-deploy/tarball | tar
xvz -C tempfolder --strip-components=1 && \  
mv tempfolder/ecs-deploy /usr/bin/ecs-deploy && \  
chmod +x /usr/bin/ecs-deploy && \  
rm -rf tempfolder  
  
# add slacktee  
# https://github.com/course-hero/slacktee  
RUN mkdir tempfolder && \  
curl -L https://api.github.com/repos/course-hero/slacktee/tarball | tar xvz -C
tempfolder --strip-components=1 && \  
mv tempfolder/slacktee.sh /usr/bin/slacktee && \  
chmod +x /usr/bin/slacktee && \  
rm -rf tempfolder  
  
COPY scripts/ /usr/bin/  
  
ENTRYPOINT []  
  

