FROM gliderlabs/alpine:latest  
  
LABEL maintainer=dansta  
  
ARG BIND_COMPILEDDIR  
ENV BIND_COMPILEDDIR ${BIND_COMPILEDDIR:-/var/named}  
ARG BIND_SOURCEDIR  
ENV BIND_SOURCEDIR ${BIND_SOURCEDIR:-/var/bind}  
ARG WORKDIRS  
ENV WORKDIRS ${WORKDIRS:-/etc/named/ \  
/var/log/named/ \  
/var/bind/ \  
${BIND_COMPILEDDIR} \  
${BIND_SOURCEDIR}}  
ARG PERMANENT_APPLICATIONS  
ENV PERMANENT_APPLICATIONS ${PERMANENT_APPLICATIONS:-bind \  
ca-certificates}  
ARG REMOVABLE_APPLICATIONS  
ENV REMOVABLE_APPLICATIONS ${REMOVABLE_APPLICATIONS:-python3}  
ARG BIND_CONF  
ENV BIND_CONF ${BIND_CONF:-/etc/bind/named.conf.recursive}  
ARG BIND_PORT  
ENV BIND_PORT ${BIND_PORT:-53}  
ARG BIND_ROOT_SERVERS  
ENV BIND_ROOT_SERVERS ${BIND_ROOT_SERVERS:-named.ca}  
ARG BIND_LOCALHOST_ZONE  
ENV BIND_LOCALHOST_ZONE ${BIND_LOCALHOST_ZONE:-pri/localhost.zone}  
ARG BIND_LOCALHOST_127  
ENV BIND_LOCALHOST_127 ${BIND_LOCALHOST_127:-pri/127.zone}  
ARG BIND_LOCAL_NETS  
ENV BIND_LOCAL_NETS
${BIND_LOCAL_NETS:-10.0.0.0/8;172.16.0.0/12;192.168.0.0/16;}  
ARG BIND_EFFECTIVE_USER  
ENV BIND_EFFECTIVE_USER ${BIND_EFFECTIVE_USER:-named}  
ARG BIND_EFFECTIVE_GROUP  
ENV BIND_EFFECTIVE_GROUP ${BIND_EFFECTIVE_GROUP:-named}  
  
# Healthcheck is not working, disabling for now  
#HEALTHCHECK --interval=10s --timeout=3s CMD dig @localhost
www.kvantmekanik.se || exit 1  
# Create confdirs  
RUN mkdir -p ${WORKDIRS}  
  
# Update cache and install packages  
RUN apk update && apk --no-cache add ${PERMANENT_APPLICATIONS} \  
${REMOVABLE_APPLICATIONS}  
  
# Change user  
#RUN adduser ${BIND_EFFECTIVE_USER} -D -H -s /usr/sbin/nologin  
ADD files/named.conf ${BIND_CONF}  
ADD files/wrapper.sh /usr/bin/wrapper.sh  
ADD files/replace.py /usr/local/bin/replace_conf  
RUN chmod +rx /usr/local/bin/replace_conf /usr/bin/wrapper.sh  
RUN /usr/local/bin/replace_conf ${BIND_CONF} BIND  
RUN /usr/local/bin/replace_conf /usr/bin/wrapper.sh BIND  
RUN rm -f /usr/local/bin/replace_conf  
  
# Permissions  
RUN chown -R ${BIND_EFFECTIVE_USER}:${BIND_EFFECTIVE_GROUP} ${WORKDIRS}  
# This one requires special treatment  
RUN chmod -R go-rw /var/log/named  
  
# Mount volumes to keep store and logs away from the thin layer overlay  
# This is important for performance and memory footprint  
VOLUME /var/log/named/ \  
/var/named/ \  
/var/bind/  
  
RUN cp /var/bind/pri/* /var/named/ && \  
mv /var/named/127.zone /var/named/0.0.127.in-addr.arpa && \  
mv /var/named/localhost.zone /var/named/master.localhost  
  
# Remove this line if you want to be able to rerun replace_conf  
# to enable runtime environment variables being read into the application  
# Otherwise we do not need this package for runtime activities  
# Replace_conf might become a standalone binary in the future  
RUN apk del ${REMOVABLE_APPLICATIONS}  
# Document port usage for docker in case you are going to use it as a service  
EXPOSE ${BIND_PORT}/tcp \  
${BIND_PORT}/udp  
  
  
# Test squid for build  
CMD /usr/bin/wrapper.sh  

