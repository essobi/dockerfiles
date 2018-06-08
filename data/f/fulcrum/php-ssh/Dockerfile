FROM fulcrum/php  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
# install ssh, setup restricted bash and change php user's shell to it  
RUN rpm --rebuilddb && \  
yum --noplugins install -y openssh-clients && \  
yum --noplugins upgrade -y && \  
package-cleanup --dupes && \  
package-cleanup --cleandupes && \  
yum clean all && \  
ln -s /bin/bash /bin/rbash && chsh -s /bin/rbash php

