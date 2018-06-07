# Create by Xie Xianbin, For Jekyll-hook Dockerfile  
# v 0.0.1  
# base image  
FROM jekyll/jekyll:3.6.2  
# remark  
MAINTAINER Xie Xianbin "me@xiexianbin.cn"  
# Dockerfile build cache  
ENV REFRESHED_AT 2018-02-03  
WORKDIR /srv/  
  
ENV TIME_ZONE Asiz/Shanghai  
  
# for Dependencies Installation  
RUN apk update \  
&& apk add --no-cache tzdata \  
&& echo "${TIME_ZONE}" > /etc/timezone \  
&& ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \  
&& mkdir /srv/website \  
&& mkdir /srv/logs \  
&& chmod a+w /srv/logs -R \  
&& ln -s /usr/bin/node /usr/bin/nodejs \  
&& npm config set unsafe-perm true \  
&& npm install -g forever \  
&& gem install rdiscount json bundle listen rouge \  
&& apk add nginx openrc openssh --no-cache \  
&& sed -i '/need net/g' /etc/init.d/nginx \  
&& rm /etc/nginx/conf.d/default.conf -f \  
&& echo "Working, ref: https://github.com/xiexianbin/jekyll-hook-docker" >>
/var/lib/nginx/html/index.html \  
&& rc-update add nginx boot \  
# && rc-service nginx restart \  
&& openrc boot \  
&& git clone https://github.com/xiexianbin/jekyll-hook.git \  
&& cd jekyll-hook \  
&& npm install  
  
# Configuration  
COPY configs/config.json ./jekyll-hook/  
COPY configs/config /root/.ssh/  
COPY configs/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY configs/etc/nginx/conf.d/jekyll_hook.conf
/etc/nginx/conf.d/jekyll_hook.conf  
COPY configs/etc/nginx/conf.d/REPO_NAME_GITHUB_IO.conf ./  
COPY run.sh ./  
RUN chmod a+x /srv/run.sh  
  
EXPOSE 80  
CMD ["/srv/run.sh"]  
ENTRYPOINT [ "bash", "-c" ]  

