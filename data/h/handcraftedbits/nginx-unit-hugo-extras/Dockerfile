FROM handcraftedbits/nginx-unit-hugo:v0.28  
MAINTAINER HandcraftedBits <opensource@handcraftedbits.com>  
  
RUN apk update && \  
apk add curl jq nodejs py-pip && \  
npm install -g bower gulp-cli grunt-cli && \  
  
pip install -U pip && \  
pip install Pygments  

