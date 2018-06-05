FROM golang:1.7-alpine  
MAINTAINER PA Infrastructure <pa_ife@peopleadmin.com>  
  
ENV GLIDE=0.12.3  
ENV REPO_PATH=bitbucket.org/peopleadmin/bb-core  
ENV SVC_NAME=chef_service  
  
EXPOSE 8080  
RUN apk update && apk add curl git && rm -rf /var/cache/apk/*  
  
# Install Glide for Dep Management  
ADD
https://github.com/Masterminds/glide/releases/download/v${GLIDE}/glide-v${GLIDE}-linux-
amd64.tar.gz /tmp/  
RUN tar -C /tmp -xzf /tmp/glide-v${GLIDE}-linux-amd64.tar.gz \  
&& cp /tmp/linux-amd64/glide /usr/local/bin/ \  
&& rm -rf /tmp/*  
  
# Install the Application  
COPY ./glide.* /go/src/${REPO_PATH}/  
COPY ./cmd /go/src/${REPO_PATH}/cmd  
COPY ./pkg /go/src/${REPO_PATH}/pkg  
RUN cd /go/src/${REPO_PATH} && glide install && go install
./cmd/${SVC_NAME}/... && rm -rf /go/src/${REPO_PATH}  
  
CMD ${SVC_NAME}

