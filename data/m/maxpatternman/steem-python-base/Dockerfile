FROM python:3-alpine3.7  
  
# install dependencies  
RUN apk add \--no-cache openssl-dev \  
build-base \  
git \  
&& git clone https://github.com/steemit/steem-python.git \  
&& cd steem-python \  
&& python setup.py install \  
&& rm -r /steem-python \  
&& apk del build-base \  
git  
  
LABEL maintainer="Max Patternman (https://github.com/maxpatternman)" \  
source="https://github.com/steemit/steem-python"  

