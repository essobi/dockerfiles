# GENERATED FILE -- DO NOT EDIT.  
# See Dockerfile.tmpl  
FROM buildpack-deps:jessie-scm  
MAINTAINER qa@docker.com  
  
ENV OUTPUT_DIR /output  
ENV GOPATH /go  
VOLUME /output  
  
RUN apt-get update && apt-get install -y \  
build-essential libtool && \  
rm -rf /var/lib/apt/lists/*  
  
ENV GOVERSION 1.9  
RUN curl -sL -o /usr/bin/gimme https://raw.githubusercontent.com/travis-
ci/gimme/master/gimme && \  
chmod +x /usr/bin/gimme && \  
gimme 1.9 && \  
gimme 1.8 && \  
gimme 1.7.1 && \  
gimme 1.7 && \  
gimme 1.6.2 && \  
gimme 1.6.1 && \  
gimme 1.6 && \  
gimme 1.5.4 && \  
gimme 1.5.3  
  
RUN eval "$( gimme 1.9 )" && \  
go get github.com/golang/lint/golint && \  
go get github.com/fzipp/gocyclo && \  
go get github.com/axw/gocov/gocov && \  
go get github.com/AlekSi/gocov-xml && \  
go get github.com/jstemmer/go-junit-report && \  
go get github.com/gordonklaus/ineffassign && \  
go get github.com/GoASTScanner/gas  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  

