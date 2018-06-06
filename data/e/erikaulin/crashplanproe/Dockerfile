FROM java:openjdk-8-jre  
MAINTAINER Erik Aulin <erik@aulin.co>  
  
# install prereqs  
#RUN apk add --update wget curl sed coreutils tar bash  
RUN apt-get update \  
&& apt-get -qy --no-install-recommends install \  
cpio \  
curl \  
sed \  
wget \  
&& apt-get -q -y clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* \  
&& rm -rf /usr/share/man/?? /usr/share/man/??_*  
  
# Expose the ports and set up volumes for the data  
EXPOSE 4282 4283 4285 4286  
VOLUME ["/var/log/proserver","/var/opt/proserver","/opt/proserver"]  
  
# Copy proserver.sh install and start script due to size of Code42 server
(around 2gb)  
# Code42 Server is downloaded first time you start the container.  
COPY ./proserver.sh /  
ENTRYPOINT ["/proserver.sh"]  

