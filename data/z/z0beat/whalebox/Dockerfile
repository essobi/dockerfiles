FROM python:3-alpine  
  
ENV WHALEBOX_HOME /opt/whalebox  
ENV WHALEBOX_CONF /opt/whalebox/conf  
ENV WHALEBOX_INSTALL_DIR=/install  
ENV WHALEBOXES ${WHALEBOX_CONF}/whaleboxes.yaml  
  
ADD whalebox ${WHALEBOX_HOME}  
WORKDIR ${WHALEBOX_HOME}  
RUN mkdir -p ${WHALEBOX_INSTALL_DIR} && \  
python setup.py install  
  
ENTRYPOINT ["whalebox"]

