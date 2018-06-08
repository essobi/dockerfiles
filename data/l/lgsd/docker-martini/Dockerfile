# Dockerfile for Martini/GOLANG 1.2  
# on Ubuntu 13.10 (Saucy Salamander)  
#  
# VERSION 1.0  
# Ubuntu image built with Debian’s tool Debootstrap  
FROM lgsd/saucy  
  
MAINTAINER Luca G. Soave <luca.soave@gmail.com>  
  
# To force the upgrade of all the next packages  
# change REFRESHED_AT date, from time to time  
ENV REFRESHED_AT 2014-02-03  
# Make sure the package repository is up to date  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \  
apt-get -qq update && \  
apt-get -y upgrade && \  
apt-get install -y wget tar ca-certificates git  
  
# Download the archive (go1.2 for linux-amd64) and extract it  
# into /usr/local, creating a Go tree in /usr/local/go  
RUN wget https://go.googlecode.com/files/go1.2.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.2.linux-amd64.tar.gz && \  
rm go1.2.linux-amd64.tar.gz  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set GOPATH/GOROOT environment variables  
ENV GOPATH /go  
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin  
  
# Install the Martini package  
RUN go get github.com/codegangsta/martini  
  
# Follow the README @ https://github.com/codegangsta/martini  
# creating the first "server.go" to test the installation  
ENV FILE $HOME/server.go  
RUN echo 'package main' > $FILE && \  
echo 'import "github.com/codegangsta/martini"' >> $FILE && \  
echo 'func main() {' >> $FILE && \  
echo ' m := martini.Classic()' >> $FILE && \  
echo ' m.Get("/", func() string {' >> $FILE && \  
echo ' return "Hello world!"' >> $FILE && \  
echo ' })' >> $FILE && \  
echo ' m.Run()' >> $FILE && \  
echo '}' >> $FILE  
  
# You will now have a Martini webserver running on localhost:3000  
EXPOSE 3000  
# Start the server  
CMD ["go", "run", "server.go"]  
  

