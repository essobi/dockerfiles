FROM openjdk:jre-alpine  
MAINTAINER florian.sachs@gmx.at  
  
ENV LOGSNIFFER_VERSION=0.5.6  
ENV LOGSNIFFER_HTTP_PORT=8099  
ENV LOGSNIFFER_LISTEN_ADDRESS=127.0.0.1  
ENV LOGSNIFFER_HOME=/logsniffer  
  
#  
# Install necessary utilities incl. tini  
#  
#  
# Add tini, the entrypoint and the source_container_env.sh  
#  
RUN apk --update add wget bash ca-certificates vim  
RUN apk add --update --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ tini  
ADD entrypoint.sh /  
ADD source_container_env.sh /etc/profile.d  
RUN chmod 0755 /entrypoint.sh && \  
mkdir /logs  
  
#  
# supervisord from https://github.com/enil/alpine-supervisord-
docker/blob/master/Dockerfile  
#  
RUN apk update && apk add -u python py-pip  
RUN pip install supervisor  
  
#  
# Add logsniffer user ans war  
#  
RUN addgroup -g 8099 logsniffer && \  
adduser -s /bin/bash -G logsniffer -D -u 8099 logsniffer  
RUN wget
https://github.com/logsniffer/logsniffer/releases/download/${LOGSNIFFER_VERSION}/logsniffer.war
-O logsniffer.war && \  
mkdir ${LOGSNIFFER_HOME} && \  
chown logsniffer:logsniffer /logsniffer.war ${LOGSNIFFER_HOME}  
  
#  
# Nginx  
#  
RUN apk add nginx && \  
mkdir /run/nginx  
ADD nginx.conf /etc/nginx/nginx.conf  
RUN p=$(echo changeme|mkpasswd) && \  
echo "logsniffer:$p" > /etc/nginx/logsniffer.htpasswd  
ADD selfsigned_cert.pem /etc/nginx/cert.pem  
ADD selfsigney_key.pem /etc/nginx/privkey.pem  
RUN chmod 0640 /etc/nginx/cert.pem /etc/nginx/privkey.pem && \  
chown nginx:nginx /etc/nginx/cert.pem /etc/nginx/privkey.pem  
  
#  
# Supervisord config  
#  
ADD supervisord.conf /etc/  
  
#  
#  
# Remove obsolete tmp and chache files  
#  
RUN rm -fr /tmp/* /var/cache/apk/*  
  
EXPOSE 443  
VOLUME [ "${LOGSNIFFER_HOME}" ]  
ENTRYPOINT [ "/sbin/tini", "--", "/entrypoint.sh" ]  
CMD [ "/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf" ]  

