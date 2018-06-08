FROM debian:jessie  
  
MAINTAINER Damián Silvani <munshkr@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ruby \  
ruby-dev \  
libffi-dev \  
build-essential \  
&& apt-get clean  
  
RUN gem install \  
bundler \  
xi-lang \  
xi-supercollider \  
xi-midi  
  
CMD ["xi"]  

