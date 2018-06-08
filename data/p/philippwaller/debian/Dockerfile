FROM debian:stretch  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="Debian" \  
org.label-schema.description="Debian"  
  
ENV TZ=Europe/Berlin \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
DEBIAN_FRONTEND=teletype \  
TERM=xterm  
  
RUN DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
curl \  
dirmngr \  
gnupg2 \  
procps \  
locales \  
nano \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install locales  
RUN sed -i 's/^# *\\(en_US.UTF-8\\)/\1/' /etc/locale.gen && locale-gen  
  
# Install debug script  
COPY overlay/debug.sh /debug.sh  
RUN chmod +x /debug.sh  
  
CMD /bin/bash  

