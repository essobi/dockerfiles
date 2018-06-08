FROM debian  
MAINTAINER Tobias Raatiniemi <raatiniemi@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install -y quassel-core  
  
USER quasselcore  
  
EXPOSE 4242  
VOLUME "/var/lib/quassel"  
WORKDIR "/var/lib/quassel"  
  
CMD ["quasselcore", "--configdir=/var/lib/quassel/"]  

