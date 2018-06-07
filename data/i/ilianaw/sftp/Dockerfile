FROM alpine:latest  
RUN apk add --no-cache openssh && mkdir /etc/ssh/keys  
VOLUME ["/data", "/host_keys", "/user_keys"]  
ADD sshd_config /etc/ssh/sshd_config  
ADD run.sh generate-host-keys update-users /usr/local/bin/  
CMD ["run.sh"]  
EXPOSE 22  

