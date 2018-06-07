FROM node:6  
ENV APT_LISTCHANGES_FRONTEND mail  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y -o DPkg::options::='--force-confdef'
-o Dpkg::Options::='--force-confold' \  
curl \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y -o DPkg::options::='--force-confdef'
-o Dpkg::Options::='--force-confold' \  
yarn \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  

