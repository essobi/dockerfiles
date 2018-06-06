FROM lorislab/wildfly:11.0.0  
MAINTAINER Andrej Petras, andrej@lorislab.org  
  
USER wildfly  
  
COPY libclingo.so ${WORKDIR}  
  
COPY ./*.war ${DEPLOYMENT_DIR}  

