FROM phusion/baseimage:latest  
ARG NPM_TOKEN  
  
CMD ["/sbin/my_init"]  
  
ENV VERSION=1.12.1  
ENV DIST=-0+xenial0  
  
RUN mkdir -p /opt/nginx-vt \  
&& cd /opt/nginx-vt \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& curl -sL https://github.com/vozlt/nginx-module-vts/archive/v0.1.15.tar.gz |
tar -zx \  
&& nginx=stable \  
&& add-apt-repository -s -y ppa:nginx/$nginx \  
&& apt-get update -y \  
&& apt-get install -y dpkg-dev build-essential \  
&& mkdir /opt/nginx \  
&& cd /opt/nginx \  
&& apt-get source -y nginx=${VERSION}-0 \  
&& apt-get build-dep -y nginx=${VERSION} \  
&& cd nginx-${VERSION} \  
&& sed -i '/common_configure_flags := \\\/a \  
\--add-module=\/opt\/nginx-vt\/nginx-module-vts-0.1.15 \\\' debian/rules \  
&& dpkg-buildpackage -b \  
&& cd /opt/nginx \  
&& dpkg -i nginx-common_${VERSION}${DIST}_all.deb \  
&& dpkg -i libnginx-mod-* \  
&& dpkg -i nginx-full_${VERSION}${DIST}_amd64.deb \  
&& apt-get install -yf \  
&& apt-get remove \--purge -y dpkg-dev build-essential *-dev && rm -rf
/var/lib/apt/lists/* \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& cd / \  
&& rm -rf /var/lib/cache /var/lib/log /opt/nginx* /etc/nginx/sites-
enabled/default

