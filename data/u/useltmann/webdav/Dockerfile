FROM debian:jessie  
MAINTAINER ulf.seltmann@metaccount.de  
EXPOSE 80 443  
VOLUME ["/app"]  
ENTRYPOINT ["/docker/entrypoint"]  
CMD ["run"]  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y locales nginx nginx-
extras lighttpd-mod-webdav apache2 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV APP_USER=app \  
APP_HOME=/app \  
CLIENT_MAX_BODY_SIZE=500M \  
PWFILE=/etc/htpasswd \  
HTUSER="" \  
HTPASSWORD=""  
COPY assets/init /docker/init  
COPY assets/build /docker/build  
RUN chmod 755 /docker/init \  
&& /docker/init \  
&& rm -rf /docker/build  
  
COPY assets/setup /docker/setup  
COPY assets/entrypoint /docker/entrypoint  
RUN chmod 755 /docker/entrypoint

