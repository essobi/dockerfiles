FROM jenkinsci/jnlp-slave:alpine  
MAINTAINER Hank Jacobs <hank@distillery.com>  
  
ENV KUBECTL_VERSION 1.3.6  
ENV PATH /usr/bin:$PATH  
  
USER root  
  
RUN apk update  
RUN apk add docker  
RUN apk add py-pip  
RUN apk add curl  
  
RUN pip install awscli  
  
RUN curl -s -L https://storage.googleapis.com/kubernetes-
release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o
/usr/bin/kubectl && \  
chmod +x /usr/bin/kubectl && \  
kubectl version --client  

