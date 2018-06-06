FROM debian:stretch  
  
MAINTAINER F4BUG <f4bug@amsat.org>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends -yy \  
coccinelle \  
findutils \  
git && \  
apt-get clean  
  
ENTRYPOINT ["spatch"]  
  
CMD ["--version"]  
  
# vim: set syntax=dockerfile:  

