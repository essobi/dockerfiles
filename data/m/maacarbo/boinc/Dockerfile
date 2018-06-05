FROM ubuntu:16.04  
MAINTAINER Maarten Carbonez <maarten.carbonez@gmail.com>  
  
# Install BOINC  
RUN apt-get update --quiet \  
&& apt-get install \  
\--yes \  
\--no-install-recommends \  
\--no-install-suggests \  
boinc-client  
  
# Set working directory  
WORKDIR /var/lib/boinc-client  
# Run BOINC by default. Expects env vars for url and account key  
CMD /etc/init.d/boinc-client start; sleep 5; /usr/bin/boinccmd
--project_attach ${boincurl} ${boinckey}; tail -f /var/lib/boinc-
client/std*.txt  
  

