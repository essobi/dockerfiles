FROM golang:1.6.2  
WORKDIR /kubernetes  
COPY . /kubernetes  
ENV KUBERNETES_CONTRIB mesos  
RUN make  

