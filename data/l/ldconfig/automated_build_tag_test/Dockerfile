FROM centos:6.8  
RUN echo -e '#!/bin/bash\n' > /test.sh  
RUN echo " echo this is version 5" >> /test.sh  
RUN chmod 755 /test.sh  
ENTRYPOINT [ "bash", "/test.sh" ]  
  

