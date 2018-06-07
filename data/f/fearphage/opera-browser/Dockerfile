# Base docker image  
FROM debian:sid  
MAINTAINER fearphage <fearphage+dockerfiles@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV CHANNEL stable  
ENV OPERA_CHANNEL opera-$CHANNEL  
  
# Install Opera  
RUN apt-get update \  
&& apt-get install -y \  
ca-certificates \  
wget \  
&& echo "deb http://deb.opera.com/${OPERA_CHANNEL}/ stable non-free" >
/etc/apt/sources.list.d/opera.list \  
&& wget -qO- http://deb.opera.com/archive.key | apt-key add - \  
&& apt-get update \  
&& apt-get install -y \  
${OPERA_CHANNEL} \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY local.conf /etc/fonts/local.conf  
  
# Autorun Opera  
ENTRYPOINT [ "/usr/bin/${OPERA_CHANNEL}" ]  
CMD [ "--user-data-dir=/data", "--no-sandbox" ]  

