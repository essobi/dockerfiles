FROM mustardgrain/base:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
RUN \  
add-apt-repository -y ppa:webupd8team/java ; \  
apt-get update ; \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections ; \  
apt-get install -y oracle-java8-installer  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

