FROM ubuntu:trusty  
MAINTAINER Lucas Park <blackss3@gmail.com>  
  
# Update ubuntu  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main restricted" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install basic packages  
RUN apt-get -qq -y install git  
RUN apt-get -qq -y install curl  
#RUN apt-get -y install python2.7-minimal=2.7.3-0ubuntu3 python2.7
python2.7-minimal=2.7.3-0ubuntu2 python  
#RUN debconf-set-selections <<< 'mysql-server mysql-server/root_password
password the9700net'  
#RUN debconf-set-selections <<< 'mysql-server mysql-server/root_password_again
password the9700net'  
#RUN apt-get -qq -y install mysql-server  
# Compile libraries  
RUN apt-get -qq -y install software-properties-common  
RUN add-apt-repository -y ppa:mercurial-ppa/releases  
RUN apt-get update  
RUN apt-get -qq -y --force-yes install gcc make ssh mercurial git
libc6=2.19-0ubuntu6 libc6-dev  
RUN rm -rf /var/lib/apt/lists/*  
  
# Install golang  
ENV GOLANG_VERSION 1.4.1  
ENV GOROOT /usr/local/go  
ENV GOBIN $GOROOT/bin  
ENV PATH $PATH:$GOBIN  
ENV HOME /root  
RUN mkdir $HOME/go.lib  
ENV GOPATH $HOME/go.lib  
RUN mkdir -p $GOPATH/src  
ENV PATH $PATH:$GOPATH/bin  
RUN curl -sSL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz | tar -v -C
/usr/local -xz  
RUN cd /usr/local/go/src && ./make.bash --no-clean 2>&1  
WORKDIR $HOME  

