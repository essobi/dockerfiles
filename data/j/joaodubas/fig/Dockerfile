# fig cli  
#  
# VERSION: see `TAG`  
FROM debian:wheezy  
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"  
# install system deps  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes --no-install-recommends install curl \  
&& curl \  
\--insecure \  
-L https://github.com/docker/fig/releases/download/1.0.0/fig-`uname -s`-`uname -m` \  
-o /usr/local/bin/fig \  
&& chmod 755 /usr/local/bin/fig \  
&& apt-get -y -qq --force-yes purge curl \  
&& apt-get -y -qq --force-yes autoremove \  
&& apt-get -y -qq --force-yes clean  
  
# config container  
ENTRYPOINT ["fig"]  
CMD ["--help"]  

