FROM alpine  
RUN apk upgrade --update && \  
apk add curl mysql xz bash unzip openjdk7-jre-base tar unzip && \  
curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \  
apk add --allow-untrusted /tmp/glibc-2.21-r2.apk && \  
rm /tmp/glibc-2.21-r2.apk  
  
ENV CATTLE_HOME /var/lib/cattle  
ENV DEFAULT_CATTLE_API_UI_INDEX //releases.rancher.com/ui/0.38.0  
ENV CATTLE_DB_CATTLE_DATABASE mysql  
ADD artifacts /usr/share/cattle  
  
ADD service /service  
ENV S6_SERVICE_DIR /service  
  
COPY target/*static.tar.gz /s6-statics/  
RUN cd / && for i in $(ls /s6-statics/*static.tar.gz);do tar -zxvf $i;done  
  
VOLUME ["/var/lib/cattle"]  
VOLUME ["/var/lib/mysql"]  
  
EXPOSE 8080  
ENV CATTLE_HOST_API_PROXY_MODE embedded  
ENV CATTLE_RANCHER_SERVER_IMAGE v0.31.0-rc1  
ENV CATTLE_RANCHER_COMPOSE_VERSION beta/latest  
ENV DEFAULT_CATTLE_RANCHER_COMPOSE_LINUX_URL
https://releases.rancher.com/compose/${CATTLE_RANCHER_COMPOSE_VERSION}/rancher-
compose-linux-amd64.tar.gz  
ENV DEFAULT_CATTLE_RANCHER_COMPOSE_DARWIN_URL
https://releases.rancher.com/compose/${CATTLE_RANCHER_COMPOSE_VERSION}/rancher-
compose-darwin-amd64.tar.gz  
ENV DEFAULT_CATTLE_RANCHER_COMPOSE_WINDOWS_URL
https://releases.rancher.com/compose/${CATTLE_RANCHER_COMPOSE_VERSION}/rancher-
compose-windows-386.zip  
  
EXPOSE 3306  
ENV CATTLE_CATTLE_VERSION v0.71.0  
ADD
https://github.com/rancherio/cattle/releases/download/${CATTLE_CATTLE_VERSION}/cattle.jar
/usr/share/cattle/  
RUN /usr/share/cattle/install_cattle_binaries  
  
ENV DEFAULT_CATTLE_MACHINE_EXECUTE true  
CMD ["/usr/bin/s6-svscan", "/service"]  

