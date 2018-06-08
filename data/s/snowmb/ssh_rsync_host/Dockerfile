FROM alpine  
  
RUN apk add --no-cache --update bash rsync openssh  
  
RUN mkdir -p /var/run/sshd /root/.ssh  
  
ADD docker-entrypoint.sh /usr/local/bin/  
  
EXPOSE 22  
#save ssh keys in a volume  
VOLUME /etc/ssh/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D"]  

