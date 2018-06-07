FROM debian:jessie  
  
MAINTAINER Jacob Ingalls <jacobingalls@yahoo.com>  
  
RUN apt-get update \  
&& apt-get install -y gcc make libgdbm-dev \  
&& apt-get autoremove \  
&& apt-get clean  
  
ADD http://quozl.linux.org.au/netrek/netrek-server-vanilla-2.18.0.tar.gz
netrek-server-vanilla-2.18.0.tar.gz  
  
RUN tar -xvf netrek-server-vanilla-2.18.0.tar.gz \  
&& rm netrek-server-vanilla-2.18.0.tar.gz \  
&& mv netrek-server-vanilla-2.18.0 server \  
&& cd server \  
&& ./configure \  
&& make \  
&& make install  
  
CMD /usr/local/games/netrek-server-vanilla/bin/netrekd \  
&& tail -f /usr/local/games/netrek-server-vanilla/var/log  

