# gotchas/pharo61  
FROM gotchas/pharo-base64  
#FROM gotchas/pharo-base64-vnc  
MAINTAINER CAs  
  
#Setup user and permissions  
RUN chgrp -R 0 /opt && \  
chmod -R g=u /opt  
WORKDIR /opt  
RUN adduser --disabled-password --gid 0 --gecos "MyUser" myuser  
USER myuser  
RUN chmod -R u+w,g+w /home/myuser  
ENV HOME=/opt  
  
# this VM is currently not compatible with IceBerg. use 61+vmT for that  
RUN curl get.pharo.org/64/61+vmI | bash  
#RUN curl get.pharo.org/64/61+vmT | bash  
ADD ./*.st ./  
RUN ./pharo Pharo.image st --save --quit ./CAs-ProxyEnv.st  
# RUN ./pharo Pharo.image st --save --quit ./CAs-IceBerg.st  
# RUN ./pharo Pharo.image get GitFileTree  
RUN chmod -R g=u Pharo* pharo*  
RUN echo "Pharo installed"  

