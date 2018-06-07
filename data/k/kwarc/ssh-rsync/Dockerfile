FROM alpine  
LABEL maintainer "Tom Wiesing <tom.wiesing@fau.de>"  
  
RUN apk add --no-cache openssh rsync \  
&& sed -i s/#PermitRootLogin.*/PermitRootLogin\ without-password/
/etc/ssh/sshd_config  
  
COPY entrypoint.sh /  
EXPOSE 22  
ENTRYPOINT ["/entrypoint.sh"]

