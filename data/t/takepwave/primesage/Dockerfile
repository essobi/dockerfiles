# Sage Installation from Ubuntu PPA  
#  
# VERSION 0.1  
FROM ubuntu:14.04  
MAINTAINER Hiroshi TAKEMOTO <take.pwave@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common pkg-config  
RUN apt-add-repository -y ppa:aims/sagemath  
RUN apt-get update  
RUN apt-get install -y sagemath-upstream-binary-full  
  
COPY sitecustomize.py /usr/lib/sagemath/local/lib/python2.7/site-packages/  
COPY sage_launcher /opt/sage_launcher  
  
RUN useradd --comment "Sage Math" \--user-group --groups users --create-home
sage  
RUN echo 'sage ALL=(ALL) NOPASSWD:/usr/bin/apt-get,/usr/bin/sage' >
/etc/sudoers.d/sage  
  
USER sage  
EXPOSE 8888  
CMD ["/opt/sage_launcher"]  

