FROM golang  
MAINTAINER airbusaerial  
RUN mkdir -p /tegola/  
WORKDIR /tegola/  
COPY . /tegola  
  
#Requirements to compile  
RUN mkdir -p /usr/local/go/src/github.com/airbusaerial/  
RUN cp -r /tegola/ /usr/local/go/src/github.com/airbusaerial/  
RUN mkdir -p /usr/local/go/src/github.com/BurntSushi/  
RUN cd /usr/local/go/src/github.com/BurntSushi/ && git clone
https://github.com/BurntSushi/toml.git  
  
#Compile  
RUN cd /tegola/cmd/tegola && go build -o tegola *.go  
EXPOSE 8080  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
ONBUILD COPY config.toml /tegola/  
  
ADD ./entrypoint.sh /usr/local/bin/entrypoint  
  
CMD ["entrypoint"]  
  
## In your Dockerfile you would have:  
#  
# FROM terranodo/tegola  
# COPY config.toml /tegola/  
# RUN cd /tegola  
# CMD ["./cmd/tegola/tegola", "--config=/tegola/config.toml"]  

