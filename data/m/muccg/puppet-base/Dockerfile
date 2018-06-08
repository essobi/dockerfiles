FROM muccg/ubuntu14.04-base:latest  
MAINTAINER ccg <devops@ccg.murdoch.edu.au>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install and use wget to fetch the package that does the puppetlabs repo
setup  
RUN apt-get update && apt-get install -qy --no-install-recommends \  
wget \  
&& wget --no-check-certificate https://apt.puppetlabs.com/puppetlabs-release-
trusty.deb \  
&& dpkg -i puppetlabs-release-trusty.deb \  
&& rm puppetlabs-release-trusty.deb  
  
# puppet labs repo should be configured at this layer  
RUN apt-get update && apt-get install -qy --no-install-recommends \  
puppet \  
ruby \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN env --unset=DEBIAN_FRONTEND  

