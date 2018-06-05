FROM fedora:latest  
  
ARG PYREMEDY_VERSION=0.2.1  
ARG ARAPI_VERSION=910  
ENV REMEDY_LIBS_DIR="/opt/remedy" \  
PYREMDY_TARBALL=https://github.com/fgimian/pyremedy/archive/${PYREMEDY_VERSION}.tar.gz
\  
ARAPI_URL=https://rrr.se/download/arapi/api${ARAPI_VERSION}linux.tar.gz \  
DEPS_RUNTIME="python python-pip curl" \  
DEPS_BUILD=""  
RUN dnf -y install ${DEPS_RUNTIME} ${DEPS_BUILD} \  
&& dnf -y clean all \  
&& install -d ${REMEDY_LIBS_DIR} \  
&& curl -sL ${ARAPI_URL} \  
| tar --strip-components=1 -C ${REMEDY_LIBS_DIR} -xz \  
&& echo -e '# Remedy ARS support\n\  
/opt/remedy/lib\n\  
/opt/remedy/bin'\  
> /etc/ld.so.conf.d/remedy.conf \  
&& ldconfig \  
&& curl -sL ${PYREMDY_TARBALL} \  
| tar --strip-components=1 -C ${REMEDY_LIBS_DIR} -xz \  
&& pip install ${REMEDY_LIBS_DIR} \  
&& mkdir /scripts  
  
WORKDIR /scripts  
  
VOLUME ["/scripts"]  
  
ENTRYPOINT ["/usr/bin/python"]  

