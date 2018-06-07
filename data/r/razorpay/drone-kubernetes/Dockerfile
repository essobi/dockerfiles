FROM alpine:3.7  
RUN apk --no-cache add curl \  
ca-certificates \  
bash \  
&& curl -Lo /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/$(curl -s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& chmod +x /usr/local/bin/kubectl \  
&& kubectl version --client \  
&& mkdir -p /bin/scripts  
  
COPY ./scripts /bin/scripts  
ENTRYPOINT ["/bin/bash"]  
CMD ["/bin/scripts/run.sh"]  

