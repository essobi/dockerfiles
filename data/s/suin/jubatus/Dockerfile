  
FROM ubuntu:14.04  
MAINTAINER suin "suinyeze@gmail.com"  
RUN set -x \  
&& echo "deb http://download.jubat.us/apt binary/" | tee
/etc/apt/sources.list.d/jubatus.list \  
&& apt-get update \  
&& apt-get install -y --force-yes jubatus \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
EXPOSE 9199  
ENV JUBATUS_HOME="/opt/jubatus"  
ENV PATH="${JUBATUS_HOME}/bin:${PATH}"  
ENV LD_LIBRARY_PATH="${JUBATUS_HOME}/lib:${LD_LIBRARY_PATH}"  
ENV LDFLAGS="-L${JUBATUS_HOME}/lib ${LDFLAGS}"  
ENV CPLUS_INCLUDE_PATH="${JUBATUS_HOME}/include:${CPLUS_INCLUDE_PATH}"  
ENV PKG_CONFIG_PATH="${JUBATUS_HOME}/lib/pkgconfig:${PKG_CONFIG_PATH}"  
ENV MANPATH="${JUBATUS_HOME}/share/man:${MANPATH}"  

