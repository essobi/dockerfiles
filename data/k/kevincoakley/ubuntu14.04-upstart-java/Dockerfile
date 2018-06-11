FROM ubuntu-upstart:14.04  
MAINTAINER Kevin Coakley <kcoakley@sdsc.edu>  
  
ENV container docker  
  
#  
# Add Java 8 PPA  
#  
# Don't prompt to accept the java license  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
# Install the apt-add-repository command  
RUN apt-get update; apt-get -y install software-properties-common  
RUN apt-add-repository ppa:webupd8team/java  
RUN apt-get update; apt-get -y install oracle-java8-installer; apt-get clean  
  
# Set root password to docker  
RUN echo 'root:docker' | chpasswd  
  
EXPOSE 22  
CMD ["/sbin/init"]  

