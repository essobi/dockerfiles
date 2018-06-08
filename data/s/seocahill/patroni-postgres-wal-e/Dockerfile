FROM python:3.6.4-alpine3.7  
LABEL author="Seosamh Cahill <seo@seocahill.com>"  
  
RUN \  
apk --update --no-cache add \  
build-base \  
curl \  
linux-headers \  
postgresql \  
postgresql-dev \  
&& pip install patroni[aws]

