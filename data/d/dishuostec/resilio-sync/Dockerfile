FROM dishuostec/alpine-glibc  
MAINTAINER dishuostecli "dishuostec@gmail.com"  
ARG ALPINE_REPO=http://dl-cdn.alpinelinux.org  
  
ENV TIMEZONE Asia/Shanghai  
ENV RSLSYNC_USER_NAME admin  
ENV RSLSYNC_USER_PWD admin  
  
EXPOSE 8888  
EXPOSE 55555  
RUN ver=$(cat /etc/alpine-release | awk -F '.' '{printf "%s.%s", $1, $2;}') \  
&& repos=/etc/apk/repositories \  
&& mv -f ${repos} ${repos}_bk \  
&& echo "${ALPINE_REPO}/alpine/v${ver}/main" > ${repos} \  
&& echo "${ALPINE_REPO}/alpine/v${ver}/community" >> ${repos} \  
\  
&& apk --no-cache add tzdata \  
&& ln -sf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \  
&& echo "${TIMEZONE}" > /etc/timezone \  
\  
&& apk --no-cache add wget ca-certificates \  
&& cd /tmp \  
&& wget https://download-cdn.resilio.com/stable/linux-x64/resilio-
sync_x64.tar.gz \  
&& tar xzf resilio-sync_x64.tar.gz \  
&& mv rslsync /usr/local/bin \  
\  
&& mkdir /root/.sync \  
&& mkdir /mnt/rslsync \  
\  
&& mv -f ${repos}_bk ${repos} \  
&& apk del wget ca-certificates \  
&& rm -f *  
  
COPY start.sh /root/  
  
RUN chmod a+x /root/start.sh  
  
CMD /root/start.sh  

