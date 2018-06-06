FROM codeserver/base:latest  
MAINTAINER Neil Ellis hello@neilellis.me  
  
ENV TYK_VERSION 1.4  
ENV TYK_DASH_VERSION 0.9.2  
# Redis  
RUN cd /tmp && \  
wget http://download.redis.io/redis-stable.tar.gz && \  
tar xvzf redis-stable.tar.gz && \  
cd redis-stable && \  
make && \  
make install && \  
cp -f src/redis-sentinel /usr/local/bin && \  
mkdir -p /etc/redis && \  
cp -f *.conf /etc/redis && \  
rm -rf /tmp/redis-stable* && \  
sed -i 's/^\\(bind .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(daemonize .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(dir .*\\)$/# \1\ndir \/usr\/local\/redis/' /etc/redis/redis.conf
&& \  
sed -i 's/^\\(logfile .*\\)$/# \1/' /etc/redis/redis.conf && \  
rm -rf /tmp/*  
  
# Tyk - API management  
RUN wget
https://github.com/lonelycode/tyk/releases/download/${TYK_VERSION}/tyk.linux.amd64_${TYK_VERSION}-1_all.deb
-P /tmp/ && \  
dpkg -i /tmp/tyk.linux.amd64_${TYK_VERSION}-1_all.deb && \  
rm -f /tmp/tyk.linux.amd64_${TYK_VERSION}-1_all.deb /etc/tyk/apps/*
/etc/tyk/tyk.conf && \  
wget https://github.com/lonelycode/tyk/releases/download/${TYK_VERSION}/tyk-
dashboard-amd64-v${TYK_DASH_VERSION}.tar.gz -P /tmp/ && \  
tar -xvzf /tmp/tyk-dashboard-amd64-v${TYK_DASH_VERSION}.tar.gz && mv tyk-
analytics-v${TYK_DASH_VERSION} /app/tyk_dash && rm -rf /tmp/*  
  
ADD bin/tyk.sh /etc/service/tyk/run  
ADD bin/tyk_dash.sh /etc/service/tyk_dash/run  
ADD bin/redis.sh /etc/service/redis/run  
ADD etc/ /usr/local/etc/  
ADD etc/tyk.conf.json /etc/tyk/tyk.conf  
  
RUN chmod 755 /etc/service/tyk/run /etc/service/tyk_dash/run
/etc/service/redis/run  
  
ENV SERVICE_ACCESS_TOKEN 123  
ENV GITHUB_USER neilellis  
ENV GITHUB_PROJECT codeserver-example  
ENV GITHUB_BRANCH master  
EXPOSE 8080  

