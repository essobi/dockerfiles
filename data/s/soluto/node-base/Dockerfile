FROM ubuntu  
  
MAINTAINER Asaf Kotzer <asaf@soluto.com>  
  
RUN apt-get update \  
&& apt-get install -y curl --fix-missing \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& apt-get install -y git \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install yarn \  
&& git config --global user.email "it@soluto.com" \  
&& git config --global user.name "it" \  
  
&& apt-get clean  

