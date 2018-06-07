FROM alpine:3.4  
MAINTAINER Versates <docker@versates.com>  
  
RUN apk add --update --no-cache openssh \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p ~root/.ssh && chmod 700 ~root/.ssh && chown root:root ~root/.ssh \  
&& sed -i '/^#Port/s/^#//' /etc/ssh/sshd_config \  
&& ssh-keygen -A && mkdir -p /var/run/sshd  
  
EXPOSE 22  
COPY entrypoint /usr/local/bin/  
ENTRYPOINT [ "entrypoint" ]  
CMD [ "/usr/sbin/sshd", "-D" ]  

