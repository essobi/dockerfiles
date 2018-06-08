FROM alpine:latest  
MAINTAINER Fabio Montefuscolo <fabio.montefuscolo@gmail.com>  
  
#  
# Visit the original https://github.com/macropin/docker-sshd  
#  
RUN apk update && \  
apk add openssh rsync && \  
mkdir -m 700 -p /root/.ssh && \  
sed -i -e "1iPort 22" -e "1iStrictModes no" -e "/^#/d;/^ *$/d"
/etc/ssh/sshd_config && \  
cp -a /etc/ssh /etc/ssh.cache && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 22  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]  
  

