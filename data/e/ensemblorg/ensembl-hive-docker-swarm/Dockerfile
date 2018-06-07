# This is a Dockerfile to extend the basic eHive image with the modules to  
# work under Docker Swarm  
FROM ensemblorg/ensembl-hive  
  
# Clone the repo  
RUN git clone -b master https://github.com/Ensembl/ensembl-hive-docker-
swarm.git /repo/ensembl-hive-docker-swarm  
  
# Install all the dependencies  
RUN /repo/ensembl-hive/docker/setup_cpan.Ubuntu-16.04.sh /repo/ensembl-hive-
docker-swarm  
  
# Expand PERL5LIB  
ENV PERL5LIB "/repo/ensembl-hive-docker-swarm/modules:$PERL5LIB"  
# Setup eHive (image name, and installation path)  
COPY hive_config.json /root/.hive_config.json  
  

