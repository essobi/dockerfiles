FROM node:0.10.40  
# Location of the STI scripts inside the image  
#  
LABEL io.openshift.s2i.scripts-url=image:///usr/libexec/s2i  
  
# DEPRECATED: This label will be kept here for backward compatibility  
LABEL io.s2i.scripts-url=image:///usr/libexec/s2i  
  
# Deprecated. Use above LABEL instead, because this will be removed in future
versions.  
ENV STI_SCRIPTS_URL=image:///usr/libexec/s2i  
  
# Path to be used in other layers to place s2i scripts into  
ENV STI_SCRIPTS_PATH=/usr/libexec/s2i  
  
# The $HOME is not set by default, but some applications needs this variabl  
ENV HOME=/opt/app-root/src \  
PATH=/opt/app-root/src/bin:/opt/app-root/bin:$PATH  
  
RUN mkdir -p $HOME  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
COPY bin/fix-permissions /usr/bin/fix-permissions  
RUN useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin \  
-c "Default Application User" default  
WORKDIR $HOME  
  
#ONBUILD COPY package.json $HOME/package.json  
ONBUILD RUN npm install  
ONBUILD COPY . $HOME  
ONBUILD RUN mkdir /tmp/src  
ONBUILD RUN mkdir /tmp/artifacts  
RUN chown -R 1001:0 /opt/app-root  
#RUN chown 1001:0 /usr/bin/fix-permissions  
RUN chmod +x /usr/bin/fix-permissions  
USER 1001  
#CMD [ "npm", "start" ]  
CMD $STI_SCRIPTS_PATH/run  

