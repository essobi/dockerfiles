FROM debian:9  
ENV RSPAMD_VERSION=1.6.5  
RUN apt-get update && apt-get install -y wget gnupg \  
&& wget -O - https://rspamd.com/apt-stable/gpg.key | apt-key add \- \  
&& echo "deb http://rspamd.com/apt-stable/ stretch main" >
/etc/apt/sources.list.d/rspamd.list \  
&& apt-get update \  
&& apt-get \--no-install-recommends -y install rspamd \  
&& apt-get purge -y gnupg \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
USER _rspamd  
EXPOSE 11333 11334  
CMD ["rspamd", "-f"]  

