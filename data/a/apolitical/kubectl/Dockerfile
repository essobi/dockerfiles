FROM alpine:3.7  
RUN apk add --no-cache curl  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& chmod +x kubectl \  
&& mv kubectl /usr/local/bin/kubectl  
RUN mkdir -p ~/.kube  
  
CMD ["/usr/local/bin/kubectl"]  

