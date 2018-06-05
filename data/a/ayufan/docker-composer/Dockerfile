FROM docker/compose:1.8.1  
RUN ["apk", "add", "-U", "git", "bash", "docker", "nano", "perl", "sed", "go",
"build-base"]  
RUN ["git", "config", "--global", "receive.denyCurrentBranch",
"updateInstead"]  
RUN ["git", "config", "--global", "user.name", "Composer"]  
RUN ["git", "config", "--global", "user.email", "you@example.com"]  
  
ENV APPS_DIR=/srv/apps  
ADD /examples/ /srv/apps/  
VOLUME ["/srv/apps"]  
ENV GOPATH=/go  
ADD / $GOPATH/src/github.com/ayufan/docker-composer  
RUN cd $GOPATH/src/github.com/ayufan/docker-composer && go get -v ./... && go
build -o /usr/bin/composer  
  
ENTRYPOINT ["/usr/bin/composer"]  

