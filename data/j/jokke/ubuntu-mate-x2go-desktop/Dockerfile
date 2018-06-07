FROM jokke/ubuntu-x2go  
  
MAINTAINER Joachim Wickman <joachim@wickman.in>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
# fix so resolvconf can be configured  
RUN echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-
set-selections && \  
  
# create needed folders  
mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix && \  
  
# add Mate repositoires  
apt-add-repository -y ppa:ubuntu-mate-dev/xenial-mate > /dev/null 2>&1 && \  
apt-get update -qq && \  
  
# install Mate  
apt-get install -y --no-install-recommends ubuntu-mate-core x2gomatebindings
&& \  
  
# clean up  
apt-get clean && apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 22  

