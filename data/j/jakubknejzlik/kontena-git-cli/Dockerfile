FROM golang  
  
RUN apt-get update && \  
apt-get install ruby-full curl -y && \  
gem install kontena-cli  
  
RUN curl -fsSL https://get.docker.com/ | sh  
  
COPY . $GOPATH/src/github.com/jakubknejzlik/kontena-git-cli  
  
WORKDIR $GOPATH/src/github.com/jakubknejzlik/kontena-git-cli  
  
RUN make deploy-local  
  
ENTRYPOINT []  

