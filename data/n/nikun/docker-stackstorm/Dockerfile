FROM athlinks/ubuntu:14.04  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:nginx/stable && \  
curl -s https://packagecloud.io/install/repositories/StackStorm/staging-
stable/script.deb.sh | bash && \  
apt-get update && \  
apt-get install -y ca-certificates nginx && \  
rm -rf /var/lib/apt/lists/* && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Can find package numbers here: https://packagecloud.io/StackStorm/staging-
stable  
ENV ST2_VERSION="1.4.0-8" \  
ST2_MISTRAL_VERSION="1.4.0-8" \  
ST2_WEB_VERSION="1.4.0-1"  
  
LABEL com.stackstorm.version="${ST2_VERSION}"  
  
RUN apt-get update && \  
apt-get install -y \  
st2=$ST2_VERSION \  
st2mistral=$ST2_MISTRAL_VERSION \  
st2web=$ST2_WEB_VERSION && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -sf /dev/stdout /var/log/st2/st2api.log && \  
ln -sf /dev/stdout /var/log/st2/st2api.audit.log && \  
ln -sf /dev/stdout /var/log/st2/st2auth.log && \  
ln -sf /dev/stdout /var/log/st2/st2auth.audit.log && \  
ln -sf /dev/stdout /var/log/st2/st2garbagecollector.log && \  
ln -sf /dev/stdout /var/log/st2/st2garbagecollector.audit.log && \  
ln -sf /dev/stdout /var/log/st2/st2notifier.log && \  
ln -sf /dev/stdout /var/log/st2/st2notifier.audit.log && \  
ln -sf /dev/stdout /var/log/st2/st2resultstracker.log && \  
ln -sf /dev/stdout /var/log/st2/st2resultstracker.audit.log && \  
ln -sf /dev/stdout /var/log/st2/st2rulesengine.log && \  
ln -sf /dev/stdout /var/log/st2/st2rulesengine.audit.log && \  
ln -sf /dev/stdout /var/log/st2/st2sensorcontainer.log && \  
ln -sf /dev/stdout /var/log/st2/st2sensorcontainer.audit.log  
  
RUN rm /etc/nginx/sites-enabled/default && \  
mv /etc/nginx/nginx.conf /tmp/nginx.conf && \  
echo "daemon off;" > /etc/nginx/nginx.conf && \  
cat /tmp/nginx.conf >> /etc/nginx/nginx.conf && \  
rm /tmp/nginx.conf  
  
ADD conf/htpasswd /etc/st2/htpasswd  
  
ADD conf/nginx.conf /etc/nginx/sites-enabled/st2web.conf  
ADD conf/config.js.template /tmp/config.js.template  
ADD conf/st2.conf.template /tmp/st2.conf.template  
  
ADD bin/docker-entrypoint.sh /entrypoint.sh  
  
VOLUME [ "/etc/st2", "/opt/stackstorm/packs" ]  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

