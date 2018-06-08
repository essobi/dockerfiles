FROM busybox  
  
ENV MURMUR_VERSION=1.2.16  
ENV MURMUR_FOLDER_NAME=murmur-static_x86-${MURMUR_VERSION}  
ENV MURMUR_ARCHIVE=${MURMUR_FOLDER_NAME}.tar.bz2  
ENV MURMUR_FOLDER=/opt/${MURMUR_FOLDER_NAME}  
  
ADD https://github.com/mumble-
voip/mumble/releases/download/${MURMUR_VERSION}/${MURMUR_ARCHIVE} /tmp/  
  
RUN mkdir /opt/ && \  
tar -xvf /tmp/${MURMUR_ARCHIVE} -C /opt/ && \  
adduser -D murmur && \  
chown -R murmur:murmur ${MURMUR_FOLDER} && \  
rm /tmp/${MURMUR_ARCHIVE} && \  
mkdir -p /var/lib/murmur && \  
chown murmur:murmur /var/lib/murmur  
  
USER murmur  
  
ADD entrypoint.sh /  
  
VOLUME /var/lib/murmur  
EXPOSE 64738/tcp 64738/udp  
  
ENTRYPOINT ["/entrypoint.sh"]  

