FROM ibmjava  
MAINTAINER Victor Kulichenko <onclev@gmail.com>  
ARG TEE_CLC_VERSION  
ARG PUID=1000  
ARG PGID=1000  
ENV TEE_CLC_VERSION="${TEE_CLC_VERSION:-14.111.1}" PATH=/opt/tf:$PATH
PUID=$PUID PGID=$PGID  
RUN set -x \  
&& apt-get update -qq && apt-get install -y curl bsdtar gnome-keyring --no-
install-recommends && rm -rf /var/lib/apt/lists/* \  
&& packed="TEE-CLC-${TEE_CLC_VERSION}.zip" \  
&& curl -fSsL "https://github.com/Microsoft/team-explorer-
everywhere/releases/download/v${TEE_CLC_VERSION}/${packed}" -O \  
&& groupadd -g $PGID -r tf \  
&& useradd -b /home -m -g $PGID -u $PUID -r -s /bin/bash tf \  
&& mkdir -p /opt/tf \  
&& chown tf:tf -R /opt/tf \  
&& bsdtar -xf "${packed}" -C /opt/tf -s'|[^/]*/||' \--uid $PUID \--gid $PGID \  
&& rm "${packed}" \  
&& apt-get purge -y --auto-remove curl bsdtar  
USER tf  
RUN echo "Tweak to automatically accept tf eula (also adding the working
directory 'projects', Cache and Logs)." \  
&& set -x \  
&& mkdir -p /home/tf/projects "/home/tf/.microsoft/Team Foundation/4.0" \  
&& cd "/home/tf/.microsoft/Team Foundation/4.0" \  
&& mkdir -p Logs Cache Configuration/TEE-Mementos \  
&& cd Configuration/TEE-Mementos \  
&& printf '<ProductIdData><eula-14.0
value="true"></eula-14.0></ProductIdData>' >
"com.microsoft.tfs.client.productid.xml" \  
&& touch ".lock-com.microsoft.tfs.client.productid.xml" \  
&& tf  
WORKDIR /home/tf/projects  
VOLUME ["/home/tf/projects", "/home/tf/.microsoft/Team
Foundation/4.0/Configuration", "/home/tf/.microsoft/Team
Foundation/4.0/Cache", "/home/tf/.microsoft/Team Foundation/4.0/Logs" ]  
CMD ["tf"]  

