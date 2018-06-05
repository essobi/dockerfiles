FROM ubuntu:xenial  
MAINTAINER Fabian Köster <fabian.koester@bringnow.com>  
  
# Based on https://github.com/Hyzual/docker-gitit  
# Update package list  
RUN apt-get update -qq  
  
# Install required packages (git required by gitlab-runner)  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
mime-support gitit libghc-filestore-data ssmtp  
  
VOLUME ["/data"]  
  
VOLUME ["/etc/ssmtp"]  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
WORKDIR /data  
EXPOSE 5001  
CMD ["gitit", "-f", "/data/gitit.conf"]  

