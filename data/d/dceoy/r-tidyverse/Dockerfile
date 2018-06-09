FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN set -e \  
&& ln -sf /bin/bash /bin/sh  
  
RUN set -e \  
&& apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install apt-transport-https git libcurl4-gnutls-dev \  
libmariadb-client-lgpl-dev libpq-dev librsvg2-bin libsqlite3-dev \  
libssh2-1-dev libssl-dev libxml2-dev pandoc r-base \  
&& apt-get -y autoremove \  
&& apt-get clean  
  
RUN set -e \  
&& curl https://raw.githubusercontent.com/dceoy/clir/master/install.sh | bash  
  
RUN set -e \  
&& echo 'export PATH="${HOME}/.clir/bin:${PATH}"' >> ~/.bash_profile \  
&& source ~/.bash_profile \  
&& clir update \  
&& clir install --devt=cran dbplyr doParallel foreach gridExtra rmarkdown
tidyverse \  
&& clir validate dbplyr doParallel foreach gridExtra rmarkdown tidyverse  
  
ENTRYPOINT ["/usr/bin/R"]  

