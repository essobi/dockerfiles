#################################################################  
# Dockerfile  
# Software: miRdup  
# Software Version: 1.4  
# Description: Computational prediction of the localization of microRNAs
within their pre-miRNA  
# Website: http://cs.mcgill.ca/~blanchem/mirdup/  
# Tags: Proteomics|Genomics|General  
# Provides: miRdup V1.4  
#  
# Run : java -Xms500m -Xmx3500m -jar /miRdup/miRdup.jar -k all -r /usr/bin/  
# Run : java -jar miRdup.jar -predict -i [PATH/TO/INPUT]/infile.fasta -d
[PATH/TO/MODEL]/model.model -f [PATH/TO/OUTPUT/REP]/outfile -r /usr/bin/  
# If needed, copy new models in model folder  
# Copy: find /miRdup/ -maxdepth 1 -type f -name '*.model' -exec cp {}
[PATH/TO/MODEL] \;  
#################################################################  
  
# Base docker image  
FROM ubuntu:latest  
MAINTAINER test@armadillo.uqam  
  
# Install miRdup and dependencies  
RUN apt-get clean  
  
# Prepare installation  
RUN apt-get --quiet update \  
&& apt-get -qqy install \  
\--no-install-recommends \  
software-properties-common \  
wget \  
unzip \  
default-jre \  
default-jdk \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN apt-add-repository -y ppa:j-4/vienna-rna \  
&& apt-get --quiet update \  
&& apt-get -qqy install \  
vienna-rna \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Create rep  
RUN mkdir /miRdup /data  
  
# Get miRdup  
RUN cd ~ \  
&& wget --quiet http://cs.mcgill.ca/~blanchem/mirdup/miRdup_1.4.zip -O
miRdup_1.4.zip \  
&& unzip -qq miRdup_1.4.zip -d /miRdup \  
&& rm -f miRdup_1.4.zip  
  
RUN chmod -R +x /miRdup  
  
RUN export PATH="${PATH}:/miRdup/"  
  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
WORKDIR /data  

