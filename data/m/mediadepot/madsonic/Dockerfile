FROM mediadepot/base  
  
#Create madsonic folder structure & set as volumes  
RUN mkdir -p /srv/madsonic/app && \  
mkdir -p /srv/madsonic/data && \  
mkdir -p /srv/madsonic/config && \  
mkdir -p /srv/madsonic/transcode_lib  
  
WORKDIR /srv/madsonic/app  
  
# Install permanent apk packages  
RUN apk --update upgrade && \  
apk add openjdk8 unzip && \  
rm /var/cache/apk/*  
  
# Download & Install Madsonic  
# Then clone rolleshark theme, create war folder structure, delete tmp dir,
update war file.  
RUN mkdir -p "/srv/madsonic/data/transcode" \  
&& wget -O "/tmp/madsonic.zip"
http://madsonic.org/download/6.1/20160915_madsonic-6.1.8700-standalone.zip \  
&& wget -O "/tmp/transcode.zip"
http://madsonic.org/download/transcode/20160915_madsonic-transcode-
linux-x64.zip \  
&& unzip "/tmp/madsonic.zip" -d /srv/madsonic/app \  
&& unzip "/tmp/transcode.zip" -d /srv/madsonic/transcode_lib \  
&& rm "/tmp/madsonic.zip" \  
&& rm "/tmp/transcode.zip" \  
  
&& git clone https://github.com/ronilaukkarinen/rolleshark.git /tmp/rolleshark
\  
  
&& mkdir -p /tmp/rolleshark-theme/style \  
&& mkdir -p /tmp/rolleshark-theme/icons \  
&& mkdir -p /tmp/rolleshark-theme/WEB-INF/classes \  
&& cp /tmp/rolleshark/rolleshark-madsonic.css /tmp/rolleshark-theme/style \  
&& cp -R /tmp/rolleshark/icons/rolleshark /tmp/rolleshark-theme/icons/ \  
&& cp -R /tmp/rolleshark/webfonts /tmp/rolleshark-theme/ \  
&& cp -R /tmp/rolleshark/WEB-INF/classes/org /tmp/rolleshark-theme/WEB-
INF/classes/ \  
&& rm -rf /tmp/rolleshark \  
  
&& cd /tmp/rolleshark-theme \  
&& /usr/lib/jvm/default-jvm/bin/jar uf /srv/madsonic/app/madsonic.war *  
  
  
  
#copy over the default configuraiton & service run/finish commands  
COPY rootfs /  
  
VOLUME ["/srv/madsonic/config", "/srv/madsonic/data"]  
EXPOSE 8080  
  
ENTRYPOINT ["/init"]

