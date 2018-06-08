FROM alpine:3.4  
MAINTAINER Simon Erhardt <hello@rootlogin.ch>  
  
ARG SSHUSER="sshuser"  
RUN apk add --update \  
bash \  
curl \  
dropbear \  
dropbear-ssh \  
&& rm -rf /var/cache/apk/*  
  
COPY bin/run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
RUN mkdir -p /home/${SSHUSER}  
RUN addgroup ${SSHUSER} && adduser -s /bin/bash -G ${SSHUSER} -D -h
/home/${SSHUSER} ${SSHUSER}  
  
VOLUME ["/etc/dropbear"]  
VOLUME ["/home/${SSHUSER}"]  
  
EXPOSE 22  
ENTRYPOINT ["/usr/local/bin/run.sh"]  

