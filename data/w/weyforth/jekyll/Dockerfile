FROM ruby:2.1  
MAINTAINER "Mike Farrow" <contact@mikefarrow.co.uk>  
  
RUN apt-get update \  
&& apt-get install -y \  
node \  
python-pygments \  
&& apt-get clean  
  
ENV BUNDLE_JOBS=2 \  
BUNDLE_PATH=/bundle  
  
VOLUME /bundle  
VOLUME /src  
EXPOSE 4000  
WORKDIR /src  
  
ENTRYPOINT []  

