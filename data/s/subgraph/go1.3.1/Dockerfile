FROM ubuntu:14.04  
# Dockerfile setup (go1.3.1)  
ENV COMMIT 40272ab1339a  
  
# Setup environment  
ENV HOME /root  
ENV GOPATH /d/gopath  
ENV PATH /d/go/bin:/d/gopath/bin:$PATH  
  
# Create directories  
RUN mkdir -p /root /d/go /d/gopath /d/gopath/src  
  
# Save the Dockerfile  
ADD Dockerfile /.dockerfile  
  
# Install packages  
RUN apt-get update  
RUN apt-get install -y build-essential mercurial git-core subversion wget  
  
# Compile Go  
RUN hg clone -r $COMMIT http://code.google.com/p/go /d/go  
WORKDIR /d/go/src  
RUN bash make.bash  
  
RUN cd $gopath  

