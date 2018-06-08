FROM centos/python-27-centos7  
  
MAINTAINER Graham Dumpleton <Graham.Dumpleton@gmail.com>  
  
ENV WARPDRIVE_VERSION=0.27.0 \  
MOD_WSGI_VERSION=4.5.12  
ENV WARPDRIVE_APP_ROOT=/opt/app-root \  
WARPDRIVE_SRC_ROOT=/opt/app-root/src  
  
USER root  
RUN rm -rf ${HOME}/.pki && \  
mkdir -p ${WARPDRIVE_APP_ROOT}/.pki/nssdb && \  
usermod -d ${WARPDRIVE_APP_ROOT} default && \  
chown -R 1001:0 ${WARPDRIVE_APP_ROOT}  
USER 1001  
ENV HOME=${WARPDRIVE_APP_ROOT}  
  
RUN curl -SL -o ${WARPDRIVE_APP_ROOT}/getwarped.sh
https://raw.githubusercontent.com/GrahamDumpleton/warpdrive/master/getwarped.sh
\  
&& source scl_source enable python27 \  
&& sh -x ${WARPDRIVE_APP_ROOT}/getwarped.sh --version ${WARPDRIVE_VERSION}  
  
ENV STI_SCRIPTS_PATH=${WARPDRIVE_APP_ROOT}/s2i/bin \  
STI_SCRIPTS_URL=image://${WARPDRIVE_APP_ROOT}/s2i  
  
LABEL io.k8s.description="S2I builder for Python web applications (CentOS 7)."
\  
io.k8s.display-name="Python 2.7 (Warp Drive - CentOS 7)" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,python,python27,warpdrive,warpdrive-python27" \  
io.openshift.s2i.scripts-url="image://${WARPDRIVE_APP_ROOT}/s2i/bin" \  
io.s2i.scripts-url=image://${WARPDRIVE_APP_ROOT}/s2i  
  
WORKDIR ${WARPDRIVE_SRC_ROOT}  
  
CMD [ "warpdrive", "start" ]  

