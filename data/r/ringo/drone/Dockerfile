FROM ubuntu:12.10  
MAINTAINER Yoshiki Aoki <ringohub@gmail.com>  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL C  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y wget git mercurial bzr gcc make vim && \  
apt-get clean  
RUN wget --no-check-certificate -O /var/tmp/go1.2.2.linux-amd64.tar.gz
https://storage.googleapis.com/golang/go1.2.2.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf /var/tmp/go1.2.2.linux-amd64.tar.gz && \  
rm -f /var/tmp/go1.2.2.linux-amd64.tar.gz  
ENV GOPATH /opt/go  
ENV PATH $PATH:/usr/local/go/bin:${GOPATH}/bin  
RUN go get github.com/drone/drone/...  
  
WORKDIR /opt/go/src/github.com/drone/drone  
RUN sed -i -e 's/https:\/\/" + settings.GitHubDomain/http:\/\/" +
settings.GitHubDomain/g' pkg/handler/auth.go  
RUN sed -i -e "s/git:\/\/%s\/%s\/%s.git/git@%s:%s\/%s.git/" pkg/model/repo.go  
RUN make deps && make test && make build-dist  
  
EXPOSE 9090  
ENTRYPOINT bin/droned --port=":9090" \--datasource="drone.sqlite"  

