FROM ubuntu:16.04  
MAINTAINER Christian Harke <ch.harke@gmail.com>  
  
# Install requirements  
RUN apt-get update --quiet && \  
apt-get upgrade --quiet --yes && \  
apt-get install --quiet --yes \  
inadyn  
  
ENTRYPOINT inadyn --username ${username} \--password ${password}
\--dyndns_system ${dyndns_system} `echo ",${aliases}" | sed -e 's/,/ --alias
/g'`  

