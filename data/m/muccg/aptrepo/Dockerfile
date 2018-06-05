FROM muccg/debian8-base:latest  
MAINTAINER CCG <devops@ccg.murdoch.edu.au>  
  
# Project specific deps  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
reprepro \  
gnupg \  
awscli \  
procmail \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN env --unset=DEBIAN_FRONTEND  
  
VOLUME ["/data"]  
  
COPY keys /keys  
COPY repo /repo-template  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
RUN chown ccg-user:ccg-user /data  
  
# Drop privileges, set home for ccg-user  
USER ccg-user  
ENV HOME /data  
WORKDIR /data  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/bin/sh"]  

