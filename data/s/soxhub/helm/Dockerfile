FROM alpine:3.3  
MAINTAINER Rajiv Makhijani <rajiv@soxhub.com>  
  
RUN apk add --update --no-cache ca-certificates  
  
ENV VERSION v2.6.1  
ENV FILENAME helm-${VERSION}-linux-amd64.tar.gz  
  
WORKDIR /  
  
ADD http://storage.googleapis.com/kubernetes-helm/${FILENAME} /tmp  
  
RUN tar -zxvf /tmp/${FILENAME} -C /tmp \  
&& mv /tmp/linux-amd64/helm /bin/helm \  
&& rm -rf /tmp  
  
RUN /bin/helm init --client-only && /bin/helm repo update  
  
ENTRYPOINT ["/bin/helm"]  

