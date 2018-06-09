# Use builds from launchpad  
FROM rocker/tidyverse:3.3.3  
# Install  
# https://github.com/jeroen/opencpu-server/tree/master/debian#readme  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key 381BA480 \  
&& echo "deb http://cran.rstudio.com/bin/linux/debian jessie-cran3/" >
/etc/apt/sources.list.d/cran.list \  
&& apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y nano wget make devscripts apache2-dev apache2
libapreq2-dev \  
r-base r-base-dev libapparmor-dev libcurl4-openssl-dev libprotobuf-dev \  
protobuf-compiler xvfb xauth xfonts-base curl libssl-dev libxml2-dev libicu-
dev \  
pkg-config libssh2-1-dev net-tools  
  
RUN mkdir ~/tempdir && cd ~/tempdir \  
&& wget https://github.com/jeffreyhorner/rapache/archive/v1.2.8.tar.gz \  
&& tar xzf v1.2.8.tar.gz \  
&& cd rapache-1.2.8 \  
&& dpkg-buildpackage -us -uc \  
&& cd ~/tempdir \  
&& wget https://github.com/jeroenooms/opencpu-server/archive/v1.6.tar.gz \  
&& tar xzf v1.6.tar.gz \  
&& cd opencpu-server-1.6 \  
&& dpkg-buildpackage -us -uc \  
&& cd ~/tempdir \  
&& sudo dpkg -i libapache2-mod-r-base_*.deb \  
&& sudo dpkg -i opencpu-lib_*.deb \  
&& sudo dpkg -i opencpu-server_*.deb \  
&& cd ~/ && rm -r ~/tempdir  
  
RUN export ADD=shiny && bash /etc/cont-init.d/add  
  
# Apache ports  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8004  
# Define default command  
CMD service opencpu restart && /init  

