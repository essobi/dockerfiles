FROM java:8-jre  
  
COPY . /  
  
RUN { \  
set -ex; \  
  
# add user & group  
groupadd --system --gid 1000 commafeed; \  
useradd --system --uid 1000 --gid 1000 commafeed; \  
  
# install gosu  
curl \  
-o /usr/bin/gosu \  
-fsSL \  
"https://github.com/tianon/gosu/releases/download/1.8/gosu-$(dpkg --print-
architecture)"; \  
chmod +x /usr/bin/gosu; \  
chmod +x /usr/bin/start-commafeed; \  
# install commafeed  
curl \  
-o /opt/commafeed.jar \  
-fsSL \  
"https://github.com/Athou/commafeed/releases/download/2.3.0/commafeed.jar"; \  
}  
  
VOLUME /data/commafeed  
  
CMD ["start-commafeed"]

