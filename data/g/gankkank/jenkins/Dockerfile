From jenkins  
MAINTAINER Jimmy Yang <gankkank@gmail.com>  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y sudo rsync vim git python-pip locales && \  
pip install awscli  
  
RUN echo 'jenkins ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/90-jenkins  
  
# locale  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen  
RUN touch /etc/default/locale  
RUN locale-gen  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN update-locale  
  
USER jenkins  

