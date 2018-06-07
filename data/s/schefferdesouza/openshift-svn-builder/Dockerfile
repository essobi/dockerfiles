# svn-builder  
FROM openshift/origin-base  
MAINTAINER Gabriel Scheffer  
  
LABEL Name schefferdesouza/openshift-svn-builder:0.1.0  
LABEL Release svn-builder:0.1.0  
LABEL Version 0.1.0  
  
ENV TZ=America/Sao_Paulo  
ENV LC_ALL="pt_BR.utf8"  
RUN set -x && yum -y --enablerepo=centosplus install \  
docker unzip subversion && \  
yum -y clean all && \  
localedef -f UTF-8 -i pt_BR pt_BR.UTF-8 && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
ENV BUILDER_VERSION 1.0  
ADD etc/locale.conf /etc  
  
ADD build.sh /tmp/build.sh  
  
ENTRYPOINT ["/bin/sh", "-c"]  
CMD ["/tmp/build.sh"]  

