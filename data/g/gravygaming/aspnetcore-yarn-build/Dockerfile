FROM microsoft/aspnetcore-build:2.0.6-2.1.101-stretch  
LABEL Author="Gravy Gaming"  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y yarn  

