# Download the latest R-repo  
FROM r-base:latest  
  
# Update cache and install apt-utils  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
  
# Aptitude required for RCurl  
RUN apt-get install aptitude -y  
  
# Install curl  
RUN apt-get install curl libcurl4-gnutls-dev -y  
  
# Openssl required  
RUN apt-get install libssl-dev -y  
  
# Libxml2 required  
RUN apt-get install libxml2-dev -y  
  
# Cairo required  
RUN aptitude install libglib2.0-0=2.54.1-1 -y  
RUN aptitude install libglib2.0-dev -y  
RUN apt-get install libcairo2-dev -y  
  
# Cairo backend - requires version controlling  
RUN aptitude install libpango-1.0-0=1.40.12-1 -y  
RUN aptitude install libpangocairo-1.0-0=1.40.12-1 -y  
RUN aptitude install libpangoft2-1.0-0=1.40.12-1 -y  
RUN apt-get install libpango1.0-dev libgtk2.0-dev xvfb xauth xfonts-base
libxt-dev -y  
  
# 'docker' is the user in r-base  
# Change into user directory.  
WORKDIR /home/docker  
  
# Download R script  
RUN curl -o AQM.R
https://raw.githubusercontent.com/alexiswl/rnaseq_singularity_containers/master/arrayQualityMetrics_report/AQM.R  
  
# Install the arrayQualityMetrics package  
RUN Rscript -e "source('https://bioconductor.org/biocLite.R');
biocLite(c('DESeq2', 'arrayQualityMetrics'))"  
  
# Now run the AQM.R script  
ENTRYPOINT ["Rscript", "/home/docker/AQM.R"]  

