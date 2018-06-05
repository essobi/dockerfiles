FROM ubuntu:16.04  
  
EXPOSE 8080  
  
RUN apt update && apt-get install -y golang-1.9-go git && \  
export PATH=$PATH:/usr/lib/go-1.9/bin && mkdir -p /tmp/gotty && \  
GOPATH=/tmp/gotty go get github.com/yudai/gotty && \  
mv /tmp/gotty/bin/gotty /usr/local/bin/ && \  
rm -rf /tmp/gotty /var/cache/apk/*  
  
RUN apt-get install -y dnsutils curl vim python3 postgresql-client-9.5 && \  
curl --silent https://bootstrap.pypa.io/get-pip.py | python3 && pip install
--upgrade httpie && \  
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl  
  
EXPOSE 8080  
  
ENTRYPOINT ["/usr/local/bin/gotty"]  
CMD ["--permit-write","--reconnect","/bin/bash"]  

