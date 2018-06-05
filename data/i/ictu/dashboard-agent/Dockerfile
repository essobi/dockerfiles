FROM docker:1.9  
RUN apk --update --no-cache add nodejs bash jq nmap-ncat coreutils  
  
RUN curl -Ss -L
https://github.com/coreos/etcd/releases/download/v2.2.5/etcd-v2.2.5-linux-
amd64.tar.gz -o /tmp/etcd-v2.2.5-linux-amd64.tar.gz \  
&& tar xzvf /tmp/etcd-v2.2.5-linux-amd64.tar.gz -C /tmp/ \  
&& mv /tmp/etcd-v2.2.5-linux-amd64/etcdctl /usr/bin/etcdctl \  
&& rm -rf /tmp/etcd-v2.2.5-linux-amd64*  
  
ADD . /app  
  
WORKDIR /app  
  
RUN npm install  
  
EXPOSE 80  
CMD ["npm", "start"]  

