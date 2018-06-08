FROM centos:7  
# consider all options and if it wouldn't be better to skip EXPOSE if someone
wants to build non-server app  
# you can always do it manually after  
# one downside is that that using "s2i build" won't auto expose it with --run
flag  
EXPOSE 5000  
ENV HOME=/opt/app-root/src \  
STI_SCRIPTS_PATH=/usr/libexec/s2i  
  
WORKDIR ${HOME}  
  
LABEL io.openshift.s2i.scripts-url image://${STI_SCRIPTS_PATH}  
  
ADD ./s2i/ ${STI_SCRIPTS_PATH}  
  
RUN find ${HOME} -exec chgrp 0 {} \; -exec chmod g+rw {} \; -type d -exec
chmod g+x {} \;  
  
USER 1001  
CMD ${STI_SCRIPTS_PATH}/usage  

