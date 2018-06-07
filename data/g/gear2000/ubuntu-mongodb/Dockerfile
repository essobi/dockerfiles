FROM gear2000/chef-solo  
MAINTAINER Gary Leong <gwleong@gmail.com>  
  
############################################################  
RUN echo "Running Jiffy self-contained installers" && \  
mkdir /var/tmp/jiffy  
  
COPY var/tmp/docker/jiffy/tarballs/selfcontained /var/tmp/jiffy  
  
ADD install.sh /install.sh  
RUN /install.sh  
  
ADD run.sh /run.sh  
  
CMD ["/run.sh"]  

