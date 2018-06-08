FROM ubuntu:14.04  
  
LABEL MAINTAINER="Greg Junge <gregnuj@gmail.com>"  
  
RUN set -e \  
&& apt-get update \  
&& apt-get install -y \  
\--no-install-recommends \  
\--no-install-suggests \  
python-software-properties software-properties-common \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv BC19DDBA \  
&& add-apt-repository 'deb http://releases.galeracluster.com/ubuntu trusty
main' \  
&& apt-get update \  
&& apt-get install -y \  
\--no-install-recommends \  
\--no-install-suggests \  
galera-3 galera-arbitrator-3 \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["garbd"]  
  
  

