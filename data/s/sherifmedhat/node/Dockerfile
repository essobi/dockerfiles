FROM node:8-slim  
  
MAINTAINER SherifMedhat  
  
RUN apt-get update -qq && apt-get install -y build-essential  
  
RUN apt-get update && apt-get install -y \  
libfontconfig \  
git \  
python  
  
RUN set -x \  
# Upgrade npm  
# Don't use npm to self-upgrade, see issue
https://github.com/npm/npm/issues/9863  
#&& curl -L https://npmjs.org/install.sh | sh \  
# Install node packages  
&& npm install --silent -g \  
gulp-cli

