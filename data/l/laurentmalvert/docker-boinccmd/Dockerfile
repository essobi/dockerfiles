FROM laurentmalvert/docker-boinc:jessie  
  
MAINTAINER Laurent Malvert <laurent.malvert@gmail.com>  
  
LABEL \  
Vendor="Laurent Malvert" \  
Description="A base container image providing boinccmd to control clients" \  
Version="jessie_7.4.23" \  
Boinc-Version="7.4.23" \  
Base-Version="debian:jessie"  
# -- BOINC ---------------------------------------------------------------  
  
USER boinc  
  
ENTRYPOINT ["boinccmd"]  

