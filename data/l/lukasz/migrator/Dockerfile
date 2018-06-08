FROM debian:jessie  
  
MAINTAINER Łukasz Budnik lukasz.budnik@gmail.com  
  
RUN apt-get update && apt-get install -y curl git  
  
# install gimme and go 1.5 version  
RUN curl -sL -o /bin/gimme https://raw.githubusercontent.com/travis-
ci/gimme/master/gimme && chmod +x /bin/gimme && gimme 1.5  
  
# envs  
ENV GOPATH=/opt/gocode PATH=$PATH:/opt/gocode/bin  
  
# install migrator  
RUN mkdir /opt/gocode && . ~/.gimme/envs/go1.5.env && go get
github.com/lukaszbudnik/migrator  
  
VOLUME ["/data"]  
  
# copy entrypoint  
COPY docker-entrypoint.sh .  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8080  

