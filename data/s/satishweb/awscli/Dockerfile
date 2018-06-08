#!/bin/bash  
# Ubuntu + awscli Docker image  
# Type: Shell Access Based (Opens bash shell)  
# Use: Generally used to run for scripts or automation tools usages  
# Author: Satish Gaikwad <satish@satishweb.com>  
  
# To know contents of awscli Dockerfile, please open source repository on
github for this docker image.  
# Docker hub somehow can not understand how to handle multiple Dockerfiles for
display on the Docker hub image page.  
FROM satishweb/awscli  
MAINTAINER Satish Gaikwad <satish@satishweb.com>  
  
# Lets modify entrypoint.sh to remove aws command reference.  
RUN echo '#!/bin/bash'>/opt/entrypoint.sh \  
&& echo 'set -e && exec "$@"' >>/opt/entrypoint.sh  
  
# We are just running default command to open shell for scripted/automated use
of awscli  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["/bin/bash"]  

