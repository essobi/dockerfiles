# DESCRIPTION: Ahsay OBSR image  
# TO RUN (interactive): docker run -it --name obsr -p 80:80 -p 443:443 -v
/tmp/obsr/userhome:/obsr/user -v /tmp/obsr/system:/obsr/system yoff/obsr  
FROM debian:latest  
MAINTAINER HB <harry.bonneto@technolis.fr>  
  
  
# Prepare the OS  
# net-tools for ifconfig (OBSR uses it to get MAC address for licensing)  
# tmux to allow shell along side OBSR  
# nano because editing with vi hurts  
# curl to download over https with invalid cert  
RUN set -x && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install tmux net-tools curl nano && \  
apt-get autoremove && \  
apt-get autoclean  
  
EXPOSE 80 443  
# VOLUME ["/obsr/user", "/obsr/system"]  
ENV CBS_HOME /usr/local/cbs  
ENV USER_HOMES ${CBS_HOME}/users  
ENV LOG_HOMES ${CBS_HOME}/logs  
VOLUME /usr/local/cbs/users /usr/local/cbs/logs /usr/local/cbs/conf  
RUN mkdir -p $CBS_HOME  
WORKDIR $CBS_HOME  
  
# Get OBSR tarball into container (local)  
# Note: ADD untars local files automatically (COPY does not)  
ADD cbs-nix-7.5.0.0.tar.gz ./  
  
# Get OBSR tarball into container (https)  
# RUN set -x && \  
# curl -k http://ahsay-dn.ahsay.com/v7/7500/cbs-nix.tar.gz -o cbs-nix.tar.gz
&& \  
# tar xzf cbs-nix.tar.gz && \  
# rm cbs-nix.tar.gz  
# OBSR tweaks  
# 1 Remove java x86  
# 2 Prevent OBSR from daemonizing  
# 3 Restrict OBSR cipher suites (resolves weak Diffie-Helman)  
RUN set -x && \  
rm -rf $home/java-linux-x86/ && \  
sed -i 's|nohup sh "${CATALINA_HOME}/bin/catalina.sh" start > /dev/null 2>&1
&|sh "${CATALINA_HOME}/bin/catalina.sh" run|' bin/startup.sh && \  
sed -i 's|port="443"|port="443"
ciphers="SSL_RSA_WITH_RC4_128_MD5,SSL_RSA_WITH_RC4_128_SHA,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA,SSL_RSA_WITH_3DES_EDE_CBC_SHA"|'
conf/server.xml  
  
# HARDEN OBS  
# Enforce SSL; CUSTOM 40X 50X HTTP ERROR PAGES  
COPY obsr-assets/ ./  
RUN chmod -R 755 tomcat/bin  
  
# Officially install OBSR  
# install.sh gets called automatically during startup.sh (from tmux.sh)  
# RUN bin/install.sh  
# Add docker entrypoint  
COPY tmux.sh ./  
RUN chmod +x tmux.sh  
ENTRYPOINT ["/obsr/tmux.sh"]  

