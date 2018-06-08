FROM octoblu/meshblu-util  
MAINTAINER Octoblu <docker@octoblu.com>  
  
RUN apt-get update && apt-get install -y jq && rm -rf /var/lib/apt/lists/*  
RUN curl -sL
https://github.com/coreos/etcd/releases/download/v2.0.10/etcd-v2.0.10-linux-
amd64.tar.gz | tar -xz -C /opt/  
ENV PATH $PATH:/opt/etcd-v2.0.10-linux-amd64  
COPY run.sh /usr/src/app/  
  
ENTRYPOINT ["./run.sh"]  

