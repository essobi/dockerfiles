FROM blitznote/debootstrap-amd64:16.04  
MAINTAINER Patrick Double <pat@patdouble.com>  
  
ARG BUILD_DATE  
ARG SOURCE_COMMIT  
ARG DOCKERFILE_PATH  
ARG SOURCE_TYPE  
ARG VERSION=23.3-1  
RUN apt-get -q update  
RUN apt-get install -y forked-daapd avahi-daemon netcat-openbsd &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /tmp/*  
  
VOLUME [ "/cache", "/media" ]  
EXPOSE 3689  
COPY forked-daapd.conf /etc/  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
CMD ["/start.sh"]  
  
HEALTHCHECK CMD nc -zv localhost 3689 || exit 1  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="$DOCKERFILE_PATH/Dockerfile" \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.name="iTunes and Roku streaming music server" \  
org.label-schema.url="https://github.com/double16/forked-daapd" \  
org.label-schema.vcs-ref=$SOURCE_COMMIT \  
org.label-schema.vcs-type="$SOURCE_TYPE" \  
org.label-schema.vcs-url="https://github.com/double16/forked-daapd.git"  

