FROM alpine:latest  
  
MAINTAINER George Bolo <gbolo@linuxctl.com>  
  
EXPOSE 22  
#
-----------------------------------------------------------------------------  
# Install our utilities  
#
-----------------------------------------------------------------------------  
RUN apk add --no-cache supervisor mysql-client curl openssh git rsync bash  
  
#
-----------------------------------------------------------------------------  
# Prepare and configure  
#
-----------------------------------------------------------------------------  
RUN /usr/bin/ssh-keygen -A  
COPY supervisord.conf /etc/supervisord.conf  
  
#
-----------------------------------------------------------------------------  
# run supervisord  
#
-----------------------------------------------------------------------------  
CMD ["/usr/bin/supervisord"]  

