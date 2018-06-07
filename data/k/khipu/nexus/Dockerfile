FROM sonatype/nexus  
MAINTAINER developers@khipu.com  
  
USER root  
  
RUN groupmod -g 2001 nexus && \  
usermod -u 2001 -g 2001 nexus  
  
USER nexus  

