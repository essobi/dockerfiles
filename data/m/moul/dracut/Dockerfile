FROM buildpack-deps:jessie  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get -q update \  
&& apt-get -qqy upgrade \  
&& apt-get -qqy install dracut dracut-network  

