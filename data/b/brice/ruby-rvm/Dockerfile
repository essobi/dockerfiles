FROM ubuntu:12.10  
MAINTAINER Brandon Rice <brice84@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get -y install curl git  
  
RUN curl -L https://get.rvm.io | bash -s stable  
RUN echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN rvm requirements  
  
RUN /bin/bash -l -c 'rvm rvmrc warning ignore all.rvmrcs'  
  
CMD ["/bin/bash"]  

