FROM r-base  
MAINTAINER Kapeel Chougule  
LABEL Description="This image is used for Ballgown RNAseq differential
expression analysis"  
# Install dependencies  
RUN apt-get update && apt-get install -y build-essential git libxml2
libxml2-dev r-base-dev libcurl4-gnutls-dev libssl-dev apt-utils \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
# Install git and clone the ballgown tool  
# RUN apt-get install --yes git  
RUN echo 'source("https://bioconductor.org/biocLite.R")' > /tmp/packages.R \  
&& echo 'biocLite("ballgown")' >> /tmp/packages.R \  
&& echo 'biocLite("genefilter")' >> /tmp/packages.R \  
&& echo 'install.packages("getopt",dependencies = TRUE)' >> /tmp/packages.R \  
&& Rscript /tmp/packages.R  
#ENV HOME /home/user  
#WORKDIR $HOME  
#ADD ballgown.R $HOME/ballgown.R  
ADD ballgown.R /usr/bin/  
#RUN [ "chmod", "+x", "$HOME/ballgown.R" ]  
RUN [ "chmod", "+x", "/usr/bin/ballgown.R" ]  
ENTRYPOINT ["ballgown.R"]  

