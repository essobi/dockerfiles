FROM python:3-alpine  
ENV LANG C.UTF-8  
RUN apk update && apk upgrade \  
&& apk add --no-cache --virtual .fetch-deps \  
git \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
RUN pip install aiohttp  
RUN pip install -e "git+https://github.com/hankei6km/test-travis-
ci.git@master#egg=pkg"  
COPY opt/flying_tent_api /opt/flying_tent_api  

