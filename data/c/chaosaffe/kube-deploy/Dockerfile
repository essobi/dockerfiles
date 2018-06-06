FROM alpine:latest as Puller  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.10.3/bin/linux/amd64/kubectl /bin/kubectl  
RUN apk add --no-cache curl  
RUN cd /bin/ && curl http://storage.googleapis.com/kubernetes-
helm/helm-v2.9.1-linux-amd64.tar.gz | \  
tar -xvz --strip-components=1 linux-amd64/helm  
RUN chmod +x /bin/kubectl && chmod +x /bin/helm  
  
FROM alpine:latest  
RUN apk add --no-cache \  
ca-certificates \  
git  
COPY \--from=Puller /bin/kubectl /bin/helm /bin/  
RUN helm init -c  

