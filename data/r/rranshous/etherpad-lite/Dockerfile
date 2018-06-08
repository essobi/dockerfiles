FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y gzip git curl python libssl-dev pkg-
config build-essential nodejs npm  
RUN cd /usr/bin && ln -s nodejs node  
  
EXPOSE 9001  
ADD ./ /webapp  
WORKDIR /webapp  
CMD ["bin/run.sh", "--root"]  

