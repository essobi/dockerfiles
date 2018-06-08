FROM buildpack-deps:jessie-curl  
  
RUN set -x \  
&& export MM_VERSION="3.0.3" \  
&& export MM_NAME="mattermost-team-${MM_VERSION}-linux-amd64.tar.gz" \  
&& export MM_URL="https://releases.mattermost.com/${MM_VERSION}/${MM_NAME}" \  
&& mkdir -p /opt \  
&& cd /opt \  
&& curl -fsSLO ${MM_URL} \  
&& tar -xzf ${MM_NAME} \  
&& chown -R root:root mattermost \  
&& rm -f ${MM_NAME}  
  
EXPOSE 8065  
  
WORKDIR /opt/mattermost  
  

