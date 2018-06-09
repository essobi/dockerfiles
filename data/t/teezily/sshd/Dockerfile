FROM debian:jessie  
MAINTAINER Teezily <dev@teezily.com>  
  
ADD build /build  
  
ENV SSH_USER ssh_user  
ENV SSH_PASS ssh_password  
  
RUN /build/prepare.sh && \  
/build/install.sh && \  
/build/cleanup.sh  
  
ADD run /app/run  
  
EXPOSE 22  
CMD ["/app/run"]  

