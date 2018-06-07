# Docker Data-Only container to hold the ee-codeception library  
# Version 0.1  
# Author Darren Ethier  
FROM busybox  
MAINTAINER Darren Ethier (darren@eventespresso.com)  
RUN addgroup -S accuser \  
&& adduser -S -s /bin/bash -G accuser accuser \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'accuser:secret' | chpasswd  
  
CMD ["/bin/sh"]

