FROM cgrlab/tidyverse:v1.0.0-beta.1706260830  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends git  
  
RUN mkdir hpv-coinfection && cd hpv-coinfection && git init && git pull
https://86e728b5c68508d0de00422e81126de37c118fbd@github.com/cgrlab/hpv-
coinfection.git  
  
RUN echo 'remove.packages("dplyr")' | r \  
&& echo 'source("https://bioconductor.org/biocLite.R");
biocLite("VariantAnnotation"); biocLite("genoset")' | r \  
&& echo 'install.packages("humarray")' | r \  
&& echo 'require(devtools); devtools::install_github("hadley/dplyr@v0.5.0")' |
r \  
&& echo 'require(devtools); devtools::install_github("seandavi/VCFWrenchR")' |
r \  
&& echo 'require(tidyverse); sessionInfo()' | r

