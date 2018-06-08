FROM donbeave/sdkman  
  
MAINTAINER Alexey Zhokhov <alexey@zhokhov.com>  
  
ENV GRAILS_VERSION 3.0.11  
RUN set -x \  
&& /bin/bash -c "source $SDKMAN_DIR/bin/sdkman-init.sh && sdk install grails
$GRAILS_VERSION"  
  
VOLUME ["/root/.gradle", "/root/.m2", "/data"]  
  
CMD ["bash"]  

