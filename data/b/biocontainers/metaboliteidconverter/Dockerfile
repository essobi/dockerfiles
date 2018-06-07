################################  
# DockerFile to build the Parsebionet.enricment app block  
# Based on Ubuntu  
###############################  
  
# Set the base image of this container  
FROM java:8  
  
# File Author / Maintainer  
MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com
)  
  
  
ENV TOOL_VERSION v0.4  
  
  
# Image Metadata  
LABEL Description="PhenoMeNal Enrichment: open source software to cross
reference metabolite data with well known database identifiers."  
LABEL Version=$TOOL_VERSION  
  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install required package  
RUN apt-get install -y --no-install-recommends ant && \  
apt-get -y clean && apt-get -y autoremove && rm -rf /var/lib/{cache,log}/
/tmp/* /var/tmp/*  
  
  
################  
# Install Tool  
################  
  
WORKDIR /Javafiles/  
  
RUN cd /Javafiles && git clone http://vm-metexplore-
dev.toulouse.inra.fr:3000/bmerlet/parsebionet-Enrichment.git .  
  
RUN cd /Javafiles && git checkout -b tag0.4 v0.4 && ant jar  
  
  
################  
# Test Scripts  
################  
  
ADD runTest1.sh /usr/local/bin/runTest1.sh  
RUN chmod +x /usr/local/bin/runTest1.sh  
  
  
###############  
# Define EntryPoint  
################  
ENTRYPOINT ["java", "-jar", "dist/phnmnl-enrichment/phnmnl-enrichment.jar"]  

