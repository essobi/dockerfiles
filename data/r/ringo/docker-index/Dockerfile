FROM google/golang  
  
MAINTAINER Yoshiki Aoki <ringohub@gmail.com>  
  
ENV LANG en_US.UTF-8  
RUN go get github.com/revel/cmd/revel  
  
RUN go get github.com/ringohub/docker-index; echo ''  
  
ENV DOCKER_REPOSITORY_PATH /var/registry/repos  
  
RUN mkdir -p ${DOCKER_REPOSITORY_PATH}  
  
EXPOSE 9000  
CMD revel run github.com/ringohub/docker-index  
  
#CMD /bin/bash  
# docker build --rm -t ringohub/docker-index .  
# docker run -v /var/registry/repositories:/var/tmp/repos -e
DOCKER_REGISTORY_URL=foo.example.com -p 9000:9000 -ti ringohub/docker-
index:latest  

