FROM frebib/builder:latest  
MAINTAINER Joe Groocock <frebib@gmail.com>  
  
ENV CHECK_INTERVAL="*/30 * * * *" \  
CHGRP_PATHS="/config /release" \  
BUILD_ON_START="yes"  
VOLUME /config /release  
ADD bin/* /usr/local/bin/  
  
ENTRYPOINT [ "/sbin/tini", "--", "run-docker", "entrypoint" ]  
CMD [ "crond", "-f", "-l", "6", "-L", "/dev/stdout" ]  

