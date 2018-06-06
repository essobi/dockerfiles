FROM ubuntu:latest  
  
RUN apt-get -qq -y update  
RUN apt-get -qq -y install build-essential git mercurial curl subversion  
  
ENV GOVERSION=1.5  
ENV GOPATH=/go  
ENV PATH=/go/bin:/usr/local/go/bin:$PATH  
  
ADD install-go.sh /scripts/install-go.sh  
RUN bash /scripts/install-go.sh  
  
ADD install-gox.sh /scripts/install-gox.sh  
RUN bash /scripts/install-gox.sh  
  
ADD install-godep.sh /scripts/install-godep.sh  
RUN bash /scripts/install-godep.sh  
  
ADD install-govendor.sh /scripts/install-govendor.sh  
RUN bash /scripts/install-govendor.sh  
  
ADD install-gotestcover.sh /scripts/install-gotestcover.sh  
RUN bash /scripts/install-gotestcover.sh  

