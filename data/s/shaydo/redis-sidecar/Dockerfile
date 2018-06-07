FROM redis:3.2  
MAINTAINER Pavel Shaydo <pshajdo@gmail.com>  
  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.7.5/bin/linux/amd64/kubectl /usr/local/bin/kubectl  
RUN chmod +x /usr/local/bin/kubectl  
  
RUN mkdir -p /etc/pod-info && touch /etc/pod-info/labels  
  
ENV LOG_LEVEL INFO  
  
WORKDIR /app  
ADD . /app  
RUN chmod +x /app/sidecar.sh  
CMD /app/sidecar.sh  

