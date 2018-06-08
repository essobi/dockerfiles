FROM rpseq/base-longranger  
  
LABEL maintainer "ryan.smith.p@gmail.com"  
  
# Add my copy of _master  
# This change At line 16 in _master:  
# export TENX_COPYRIGHT="Copyright 2016 10x Genomics Inc All rights reserved"  
# export TENX_COPYRIGHT="Copyright_2016_10x_Genomics_Inc_All_rights_reserved"  
# Docker doesn't tolerate ENV vars with whitespace  
ADD _master /opt/longranger-2.1.2/longranger-
cs/2.1.2/tenkit/bin/common/_master  
  
# Add the docker lsf template  
ADD lsf.template /opt/longranger-2.1.2/martian-cs/2.1.1/jobmanagers  
  
# Add entrypoint script  
ADD entry.sh /opt/bin/entry.sh  
RUN chmod +x /opt/bin/entry.sh  
  
ENTRYPOINT ["/opt/bin/entry.sh"]

