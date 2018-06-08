FROM phusion/baseimage  
MAINTAINER Richard Attermeyer "richard.attermeyer@gmail.com"  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y --no-install-recommends openjdk-7-jdk  
ADD ./prepare-vagrant-user.sh /tmp/  
RUN chmod u+x /tmp/*.sh  
RUN /tmp/prepare-vagrant-user.sh  
CMD [""]  

