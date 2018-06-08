FROM phusion/passenger-customizable:0.9.18  
RUN apt-get update \  
&& /pd_build/ruby2.2.sh \  
&& /pd_build/nodejs.sh \  
&& apt-get upgrade -y -o Dpkg::Options::="--force-confold" \  
&& npm install -g npm \  
&& rm -rf /pd_build \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& gem update bundler \  
&& gem cleanup  

