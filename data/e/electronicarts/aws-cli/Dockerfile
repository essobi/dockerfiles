FROM alpine:3.4  
  
MAINTAINER Orbit Team <orbit-opensource@ea.com>  
  
ENV AWS_CLI_VERSION 1.11.91  
  
RUN apk --update --no-cache add \  
python \  
py-pip \  
groff \  
jq \  
less \  
curl \  
&& pip install awscli==$AWS_CLI_VERSION \  
&& apk del py-pip  
  
ENTRYPOINT ["aws"]

