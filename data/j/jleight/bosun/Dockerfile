FROM buildpack-deps:jessie-curl  
MAINTAINER Jonathon Leight <jonathon.leight@jleight.com>  
  
ENV BSN_VERSION 0.3.0  
ENV BSN_GITHUB https://github.com/bosun-monitor/bosun  
ENV BSN_BASEURL ${BSN_GITHUB}/releases/download/${BSN_VERSION}  
ENV BSN_PACKAGE bosun-linux-amd64  
ENV BSN_URL ${BSN_BASEURL}/${BSN_PACKAGE}  
ENV BSN_USER bosun  
ENV BSN_HOME /opt/bosun  
ENV BSN_DATA /var/opt/bosun  
  
RUN set -x \  
&& groupadd -r "${BSN_USER}" \  
&& useradd -r -g "${BSN_USER}" "${BSN_USER}" \  
&& mkdir -p "${BSN_HOME}" "${BSN_DATA}" \  
&& curl -kL -o "${BSN_HOME}/bosun" "${BSN_URL}" \  
&& chown -R "${BSN_USER}":"${BSN_USER}" "${BSN_HOME}" \  
&& chown "${BSN_USER}":"${BSN_USER}" "${BSN_DATA}" \  
&& chmod 755 "${BSN_HOME}/bosun"  
  
ADD bosun.conf /var/opt/bosun/bosun.conf  
  
USER "${BSN_USER}":"${BSN_USER}"  
WORKDIR "${BSN_DATA}"  
VOLUME ["${BSN_DATA}"]  
EXPOSE 8070  
CMD ["/opt/bosun/bosun", "-c", "/var/opt/bosun/bosun.conf"]  

