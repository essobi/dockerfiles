FROM ubuntu  
MAINTAINER kevin@pentabarf.net  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y git curl  
  
RUN curl -s https://go.googlecode.com/files/go1.2.linux-amd64.tar.gz | tar -C
/usr/local -xz  
ENV PATH /usr/local/go/bin:/go/bin:$PATH  
ENV GOPATH /go:/go/src/github.com/kevinwallace/crony/vendor  
  
ADD . /go/src/github.com/kevinwallace/crony  
RUN go install github.com/kevinwallace/crony  
  
RUN useradd -m crony  
USER crony  
WORKDIR /home/crony  
ENV HOME /home/crony  
  
RUN git config --global user.email crony@localhost  
RUN git config --global user.name Crony  
  
ENTRYPOINT ["crony", "-logtostderr"]  

