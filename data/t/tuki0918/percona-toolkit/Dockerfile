FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y \  
percona-toolkit \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
CMD ls -1 /usr/bin | grep '^pt-'  

