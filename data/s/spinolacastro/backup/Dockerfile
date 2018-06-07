FROM centos:centos7  
  
MAINTAINER Diego Castro <diego.castro@getupcloud.com>  
  
ENV BIN_DIR=/opt/backup \  
HOME=/data  
  
RUN INSTALL_PKGS="nodejs npm mariadb telnet" && \  
yum install -y epel-release && \  
yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \  
yum clean all -y  
  
RUN npm install -g azure-cli  
  
RUN mkdir -p ${HOME} ${BIN_DIR} && chmod 777 ${HOME} && chmod 555 ${BIN_DIR}  
COPY . ${BIN_DIR}  
WORKDIR ${BIN_DIR}  
  
VOLUME ${HOME}  
  
ENTRYPOINT ["container-entrypoint"]  
CMD ["run"]  
  
USER 1000  

