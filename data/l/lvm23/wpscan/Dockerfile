FROM debian:sid  
MAINTAINER Mauro <mauro@sdf.org>  
  
ENV LANG C.UTF-8  
ENV USER root  
ENV HOME /wpscan  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -yq \  
git ruby ruby-dev procps \  
libcurl4-openssl-dev make zlib1g-dev \  
ca-certificates build-essential \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/wpscanteam/wpscan.git $HOME \  
&& cd $HOME \  
&& gem install bundler \  
&& bundle install --without test \--path vendor/bundle  
  
WORKDIR $HOME  
  
ENTRYPOINT ["ruby", "/wpscan/wpscan.rb"]  

