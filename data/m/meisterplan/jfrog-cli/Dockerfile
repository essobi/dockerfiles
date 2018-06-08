FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y curl make && \  
apt-get clean  
  
RUN curl -Lo /usr/bin/jfrog https://api.bintray.com/content/jfrog/jfrog-cli-
go/\$latest/jfrog-cli-linux-amd64/jfrog?bt_package=jfrog-cli-linux-amd64  
RUN chmod +x /usr/bin/jfrog  

