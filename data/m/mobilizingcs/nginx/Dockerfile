FROM nginx:latest  
MAINTAINER Steve Nolen <technolengy@gmail.com>  
  
EXPOSE 80  
ADD docker_entrypoint.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]

