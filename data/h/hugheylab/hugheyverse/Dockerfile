FROM hugheylab/ubuntur  
  
MAINTAINER "Jake Hughey" jakejhughey@gmail.com  
  
RUN install.r devtools \  
&& r -e 'library(utils); source("https://bioconductor.org/biocLite.R");
biocLite()' \  
&& r -e 'setRepositories(ind=1:5);
devtools::install_github(paste0("hugheylab/", c("metapredict", "zeitzeiger",
"deltaccd", "limorhyde", "tipa")))' \  
&& rm -rf /tmp/downloaded_packages/  

