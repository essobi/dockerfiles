FROM golang:alpine  
  
RUN apk add \--no-cache openssh git autossh sshpass \  
&& go get -u github.com/moul/advanced-ssh-config/cmd/assh \  
&& addgroup ssh \  
&& adduser -h /config -s /bin/ash -G ssh -D ssh \  
&& mkdir -p /config/.ssh && chown -R ssh:ssh /config/.ssh  
  
USER ssh  
  
WORKDIR /config  
  
VOLUME ["/config/.ssh"]  
  
ENTRYPOINT ["/usr/bin/ssh"]  
  
CMD ["-V"]  

