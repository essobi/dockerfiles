FROM openshift/origin  
  
MAINTAINER Diego Castro <diego.castro@getupcloud.com>  
  
ENV HOME=/data \  
KUBECONFIG=/data/.kubeconfig \  
WRITE_KUBECONFIG=1 \  
CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts  
  
RUN mkdir -p ${HOME} && \  
chmod 777 ${HOME} && \  
INSTALL_PKGS="nodejs npm telnet python2-pip" && \  
yum install -y epel-release && \  
yum install -y \--setopt=tsflags=nodocs $INSTALL_PKGS && \  
yum clean all -y && \  
npm install -g azure-cli && \  
npm cache clean && \  
azure telemetry --disable && \  
azure config mode arm && \  
pip install awscli && \  
chmod 777 ${HOME} -R  
  
ADD root /  
  
#VOLUME ${HOME}  
  
USER 1000  
  
ENTRYPOINT ["container-entrypoint"]  
CMD ["run"]  

