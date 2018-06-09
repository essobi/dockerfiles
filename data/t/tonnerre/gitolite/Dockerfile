FROM alpine:3.6  
MAINTAINER Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
RUN apk update && apk add gitolite openssh openssh-client dumb-init  
  
# Enable (SSH key) logins for git user  
RUN sed -i -e's/^git:!:/git::/g' /etc/shadow  
  
COPY run-gitolite.sh /usr/local/bin/run-gitolite.sh  
RUN chmod 0555 /usr/local/bin/run-gitolite.sh  
  
USER root  
EXPOSE 22/tcp  
VOLUME ["/import", "/secrets", "/var/lib/git"]  
  
CMD ["/bin/sh", "/usr/local/bin/run-gitolite.sh"]  

