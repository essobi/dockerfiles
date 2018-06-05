FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y curl jq httpie  
  
ADD resource/ /opt/resource/  
ADD tests/ /tests/  
  
RUN curl -L
"https://cli.run.pivotal.io/stable?release=linux64-binary&version=6.27.0&source=github"
| tar -zx && mv cf /usr/bin  

