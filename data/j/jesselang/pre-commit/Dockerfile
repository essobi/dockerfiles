# pre-commit with docker support  
# http://github.com/jesselang/docker-images  
# docker pull jesselang/pre-commit  
FROM python:2-alpine  
LABEL maintainer="Jesse Lang <jesse@jesselang.com>"  
RUN apk add --no-cache \  
bash \  
docker \  
git \  
grep \  
&& pip install pre-commit>=1.0  
WORKDIR /pre-commit  
ENTRYPOINT ["/usr/local/bin/pre-commit"]  

