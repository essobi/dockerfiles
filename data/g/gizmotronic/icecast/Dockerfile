FROM alpine:3.7  
LABEL maintainer="gizmotronic@gmail.com"  
  
ENV ICECAST_VERSION 2.4.3-r5  
  
ARG user=icecast  
ARG group=icecast  
  
RUN apk -q update \  
&& apk -q --no-progress add icecast="$ICECAST_VERSION" \  
&& rm -rf /var/cache/apk/*  
  
RUN ln -fs /dev/stdout /var/log/icecast/access.log \  
&& ln -fs /dev/stderr /var/log/icecast/error.log  
  
VOLUME [ "/etc/icecast" ]  
  
EXPOSE 8000  
USER ${user}  
CMD ["icecast", "-c", "/etc/icecast/icecast.xml"]  

