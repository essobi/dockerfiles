# 本体  
#  
# VERSION 0.0.1  
  
FROM gendosu/ruby-for-rails:latest  
  
MAINTAINER Gen Takahashi "gendosu@gmail.com"  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \  
&& sudo apt-get install -y nodejs chromedriver \  
  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install yarn  

