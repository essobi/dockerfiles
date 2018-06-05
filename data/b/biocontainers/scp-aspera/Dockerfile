FROM ubuntu:16.04  
  
MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com
)  
  
  
  
RUN apt-get update -y && apt-get install -y \--no-install-recommends wget zip
&& \  
wget http://download.asperasoft.com/download/sw/ascp-client/3.5.4/ascp-
install-3.5.4.102989-linux-64.sh && \  
bash ascp-install-3.5.4.102989-linux-64.sh && \  
rm -r ascp-install-3.5.4.102989-linux-64.sh && apt-get purge -y wget && \  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
ENTRYPOINT ["ascp"]  
  

