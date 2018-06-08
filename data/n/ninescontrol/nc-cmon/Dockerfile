FROM ubuntu:16.04  
# Install ClusterControl  
RUN apt-get update  
RUN apt-get -y install wget mysql-client  
RUN wget https://severalnines.com/downloads/cmon/s9s-repo-nightly.list -P
/etc/apt/sources.list.d/  
RUN wget http://repo.severalnines.com/severalnines-repos.asc -O- | apt-key add
-  
RUN apt-get update  
RUN apt-get -y --no-install-recommends install clustercontrol-controller  
  
# Configure clustercontrol  
CMD ["cmon", "-d", "-b 0.0.0.0"]

