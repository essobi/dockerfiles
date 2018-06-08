FROM gitea/gitea:1.4.1  
LABEL maintainer "Erwin Mueller <erwin.mueller@deventm.com>"  
  
RUN set -x \  
&& apk --no-cache add \  
wget \  
rsync \  
unzip  
  
ENV PIWIK_JAVASCRIPT="" \  
GITEA_SRC_DIR="/usr/src/gitea"  
RUN set -x \  
&& cd /tmp \  
&& wget -nv -O gitea.zip https://github.com/go-gitea/gitea/archive/v1.4.1.zip
\  
&& unzip -q gitea.zip \  
&& mkdir -p /usr/src \  
&& mv gitea-1.4.1 ${GITEA_SRC_DIR} \  
&& rm gitea.zip \  
&& mkdir -p /var/www/html  
  
VOLUME ["/var/www/html"]  
  
ADD rootfs/ /  
  
RUN set -x \  
&& chmod +x /*.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/bin/s6-svscan", "/etc/s6"]  

