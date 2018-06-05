FROM rocker/rstudio  
# Note: The following is needed if starting from r-base, but doesn't work  
# because r-base is based on the 'testing' versions of Debian libraries,  
# and libcurl does not seem to be available  
# RUN apt-get install libcurl4-openssl-dev  
# Also doesn't seem to work to override the testing default  
# RUN apt-get install -o APT::Default-Release=stable libcurl4-openssl-dev  
# install octave to compute medianF0 voice feature  
RUN apt-get update && apt-get install -y \  
octave \  
octave-signal \  
libav-tools  
  
RUN Rscript -e "source('http://depot.sagebase.org/CRAN.R');
pkgInstall('synapseClient')"  
RUN Rscript -e
"install.packages(c('devtools','testthat','RJSONIO','fractal','pracma','changepoint','lomb','uuid','crayon','RCurl'),
repo='http://cran.mirrors.hoobly.com')"  
RUN Rscript -e "devtools::install_github('brian-bot/bridger')"  
RUN Rscript -e "devtools::install_github('Sage-Bionetworks/mPowerStatistics')"  
  
# Note: There are required ENV param's: SYNAPSE_USERNAME, SYNAPSE_APIKEY,
BRIDGE_USERNAME, BRIDGE_PASSWORD  
CMD "Rscript" "-e" "source(system.file('main.R',package='mPowerProcessing'))"  
  
COPY . /mPowerProcessing  
  
RUN cd /mPowerProcessing && R CMD INSTALL .  

