FROM softwareplant/base:centos  
  
ARG CONFLU_VERSION=6.0.1  
ARG CONFLU_MIN_MEM=1024  
ARG CONFLU_MAX_MEM=1024  
ARG CONFLU_CONTEXT_PATH=  
  
ARG INSTALL_DIR=/opt/atlassian/confluence  
ARG HOME_DIR=/var/atlassian/confluence  
  
ENV CONFLU_CONTEXT_PATH ${CONFLU_CONTEXT_PATH}  
ENV CONFLU_MAX_MEM ${CONFLU_MAX_MEM}  
ENV CONFLU_MIN_MEM ${CONFLU_MIN_MEM}  
  
USER root  
  
COPY ["response.varfile", "/"]  
COPY ["docker-entrypoint.sh", "/"]  
  
RUN set -x \  
&& wget --progress=dot:mega
https://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLU_VERSION}-x64.bin \  
&& chmod a+x atlassian-confluence-${CONFLU_VERSION}-x64.bin \  
&& ./atlassian-confluence-${CONFLU_VERSION}-x64.bin -q -varfile
response.varfile \  
&& rm atlassian-confluence-${CONFLU_VERSION}-x64.bin response.varfile \  
&& $INSTALL_DIR/bin/catalina.sh stop -force  
  
COPY ["setenv.sh", "$INSTALL_DIR/bin/setenv.sh.mod"]  
COPY ["server.xml", "$INSTALL_DIR/conf/server.xml.mod"]  
  
EXPOSE 8090  
EXPOSE 8091  
EXPOSE 8000  
VOLUME ["$HOME_DIR", "$INSTALL_DIR"]  
  
WORKDIR $HOME_DIR  
  
RUN chmod a+x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]

