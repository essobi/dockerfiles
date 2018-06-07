# use latest Node LTS  
FROM node:8-stretch  
  
# backport up to date tools  
RUN echo "deb http://ftp.us.debian.org/debian sid main" >>
/etc/apt/sources.list \  
&& apt-get update && apt-get install -y \  
git \  
&& apt-get clean  
  
# install Firebase CLI  
RUN yarn global add firebase-tools  

