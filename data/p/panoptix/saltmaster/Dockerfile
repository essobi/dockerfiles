FROM ubuntu  
MAINTAINER Stephan Buys <stephan.buys@panoptix.co.za>  
  
ENV REFRESHED_ON "12 Oct 2017"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install curl --yes  
RUN curl --fail --silent --show-error --location
https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub
| apt-key add -  
RUN echo 'deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial
main' > /etc/apt/sources.list.d/saltstack.list  
RUN apt-get update && apt-get install salt-master --yes  
RUN apt-get purge curl --autoremove --yes  
  
VOLUME ["/pki","/var/cache/salt","/var/log/salt"]  
EXPOSE 4505 4506  
ENTRYPOINT ["salt-master"]  
CMD ["-l","info"]  

