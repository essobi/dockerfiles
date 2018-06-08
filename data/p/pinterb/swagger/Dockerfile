FROM pinterb/base:alpine  
MAINTAINER Brad Pinter "brad.pinter@gmail.com"  
# This is the release of Swagger 2.0 cli to pull in.  
LABEL vendor="BigstickCarpet" \  
com.bigstickcarpet.swagger-cli.version="1.0.0-beta.2" \  
com.bigstickcarpet.swagger-cli.release-date="2015-09-29"  
  
ENV PUID 1000  
ENV PGID 1000  
ENV DEBUG 0  
# create dev user  
RUN apk --update add --no-cache bash nodejs sudo wget git ca-certificates && \  
addgroup -g $PGID dev && \  
adduser -h /config -u $PUID -H -D -G dev -s /bin/bash dev && \  
sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \  
sed -ri 's/# %wheel ALL=\\(ALL\\) NOPASSWD: ALL/%wheel ALL=\\(ALL\\) NOPASSWD:
ALL/' /etc/sudoers && \  
npm install -g swagger-cli  
  
RUN apk del --purge wget ca-certificates git && \  
rm -rf /var/cache/apk/*  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will  
# belong to root.  
RUN mkdir /data /output /state /config  
RUN touch /data/.extra /output/.extra /state/.extra /config/.extra  
RUN chown -R dev:dev /data && \  
chown -R dev:dev /output && \  
chown -R dev:dev /state && \  
chown -R dev:dev /config  
  
VOLUME ["/data", "/output", "/state", "/config"]  
EXPOSE 8080  
WORKDIR /data  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["--version"]  

