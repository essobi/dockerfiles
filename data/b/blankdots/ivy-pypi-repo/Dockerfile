FROM nginx:alpine  
  
MAINTAINER Stefan Negru <stefan.negru@helsinki.fi>  
  
RUN apk add --update \  
&& apk add --no-cache openjdk8-jre bash wget supervisor\  
&& rm -rf /var/cache/apk/*  
  
ARG IVY=0.7.0  
ARG PLUGIN=0.2.7  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.1/dumb-init_1.2.1_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
RUN apk --update add --no-cache --virtual build-deps gcc make musl-dev openssl
\  
&& wget -O- https://github.com/ncopa/su-exec/archive/v0.2.tar.gz | tar zxvf -
\  
&& cd su-exec-0.2 \  
&& make \  
&& mv su-exec /usr/local/bin \  
&& cd .. && rm -rf su-exec-0.2 \  
&& apk del build-deps  
  
RUN wget https://dl.bintray.com/linkedin/maven/com/linkedin/pygradle/pivy-
importer/${IVY}/pivy-importer-${IVY}-all.jar --no-check-certificate \  
&& mv pivy-importer-${IVY}-all.jar /var/lib/pivy-importer-all.jar  
  
RUN wget -P /var https://github.com/blankdots/ivy-pypi-
repo/releases/download/v${PLUGIN}/ivy-pypi-repo-${PLUGIN}.tar \  
&& tar -xf /var/ivy-pypi-repo-${PLUGIN}.tar -C /var \  
&& mv /var/ivy-pypi-repo-${PLUGIN} /var/ivy-pypi-repo  
  
# COPY nginx, supervisord specific configurations  
# default.conf is needed to have access to port 8080 as port 80 is not allowed
with  
# to be used by a user with lower privileges  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY supervisor.conf /etc/supervisor/supervisord.conf  
COPY web /var/web  
  
RUN touch /var/run/nginx.pid \  
&& mkdir -p /data  
  
# The volume needs to be set after the directory has been created to avoid  
# permissions issues  
VOLUME ["/data"]  
  
EXPOSE 5039  
EXPOSE 5639  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

