FROM ubuntu:16.04  
LABEL maintainer="Ivan Snakebot <snakebott@gmail.com>"  
  
RUN apt-get update  
RUN apt-get install -y bash wget apt-utils  
RUN bash -c 'source /etc/lsb-release && echo \  
"deb http://download.rethinkdb.com/apt \  
$DISTRIB_CODENAME main" | tee /etc/apt/sources.list.d/rethinkdb.list'  
RUN wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | apt-key add -  
RUN apt-get update && apt-get -y install rethinkdb && apt-get -y install
python3 \  
&& apt-get -y install curl && curl https://bootstrap.pypa.io/get-pip.py |
python3 \  
&& pip install rethinkdb  
  
WORKDIR /app/rethinkdb  
ADD . /app/rethinkdb  
  
VOLUME [ "/app/rethinkdb/data", "/app/rethinkdb/config" ]  
EXPOSE 28015 29015 8080  
ENTRYPOINT [ "rethinkdb"]  
CMD ["--bind", "all"]  

