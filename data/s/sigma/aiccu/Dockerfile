FROM debian:latest  
MAINTAINER Yann Hodique <yann.hodique@gmail.com>  
ENV UPDATED_AT 01-16-2015  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update  
RUN apt-get -yq install aiccu  
  
ADD start_aiccu.sh /usr/local/bin/start_aiccu.sh  
  
ENTRYPOINT ["/usr/local/bin/start_aiccu.sh"]  

