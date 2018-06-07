FROM openshift/origin  
  
MAINTAINER Mateus Caruccio <mateus.caruccio@getupcloud.com>  
  
ENV HOME=/data \  
KUBECONFIG=/data/.kubeconfig \  
CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts  
  
RUN set -x && \  
mkdir -p ${HOME} && \  
chmod 777 ${HOME} && \  
yum install -y \--setopt=tsflags=nodocs epel-release && \  
INSTALL_PKGS="gcc python34-pip python34-devel openssl-devel pv" && \  
yum install -y \--setopt=tsflags=nodocs $INSTALL_PKGS && \  
yum clean all -y && \  
pip3 install --no-cache-dir azure-storage boto3 && \  
chmod 777 ${HOME} -R  
  
ADD root /  
  
USER 1001  
  
ENTRYPOINT ["container-entrypoint"]  
CMD ["run"]  

