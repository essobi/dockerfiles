FROM ubuntu:12.04  
# Dockerfile setup  
ENV GOVER go1.2.1  
# Setup environment  
ENV HOME /root  
ENV GOPATH /d/gopath  
ENV PATH /d/go/bin:/d/gopath/bin:$PATH  
  
# Create directories  
RUN mkdir -p /root /d/go /d/gopath  
  
# Save the Dockerfile  
ADD Dockerfile /.dockerfile  
  
# Install packages  
RUN apt-get update  
RUN apt-get install -y build-essential mercurial git-core subversion wget  
  
# Compile Go  
RUN hg clone -r $GOVER http://code.google.com/p/go /d/go  
WORKDIR /d/go/src  
RUN bash make.bash  
  
# Set the normal working directory to gopath  
WORKDIR /d/gopath  

