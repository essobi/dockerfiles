FROM phusion/passenger-ruby23:0.9.19  
RUN apt-get update \  
&& apt-get upgrade -y -o Dpkg::Options::="--force-confold" \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& gem update bundler \  
&& gem cleanup  

