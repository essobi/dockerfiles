#  
# Java Oracle 7/8 Dockerfile  
#  
# https://github.com/koalabz/java-oracle.docker  
#  
# Pull base image  
#FROM dockerfile/ubuntu  
FROM koalabz/ubuntu  
MAINTAINER Karim Benbouali <karim.benbouali@koalabz.com>  
  
# Add environment variables scripts  
ADD scripts /usr/local/lib/koalabz/java-oracle/  
  
# Install Java 7  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer  
  
# Define mountable directories  
VOLUME ["/data"]  
  
# Define working directory  
WORKDIR /data  
  
# Define entrypoint and default command  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  
CMD ["bash"]  

