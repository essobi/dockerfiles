FROM alpine:3.7  
ENV VERSION v2.6.2  
RUN apk --update add curl git bash sshpass  
  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
RUN mv kubectl /usr/local/bin  
RUN chmod +x /usr/local/bin/kubectl  
RUN wget https://storage.googleapis.com/kubernetes-helm/helm-${VERSION}-linux-
amd64.tar.gz  
RUN tar -zxvf helm-${VERSION}-linux-amd64.tar.gz  
RUN mv linux-amd64/helm /usr/local/bin/helm  
RUN mkdir -p ~/.kube  
  

