FROM node:8-alpine  
  
ARG UID=1601  
ARG GID=1601  
ARG IOTA_PM_VERSION=1.2.0  
ENV IOTA_NODE="" \  
HTTP_PORT=8888  
COPY root /  
  
RUN apk --no-cache -U add \  
bash \  
su-exec \  
tini \  
&& npm install -g iota-pm@${IOTA_PM_VERSION} \  
&& addgroup -g ${GID} iota-pm \  
&& adduser -u ${UID} -h /opt/iota-pm -H -G iota-pm -s /sbin/nologin -D iota-pm  
  
VOLUME /opt/iota-pm  
  
EXPOSE 8888  
ENTRYPOINT ["/sbin/tini"]  
CMD ["/docker-run.sh"]  

