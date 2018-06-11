FROM nginx:1.10.3  
RUN echo 'deb http://deb.nodesource.com/node_6.x jessie main' >
/etc/apt/sources.list.d/nodesource.list  
RUN echo 'deb-src http://deb.nodesource.com/node_6.x jessie main' >>
/etc/apt/sources.list.d/nodesource.list  
RUN echo 'deb http://dl.yarnpkg.com/debian/ stable main' >
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1655A0AB68576280
&& \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 46C2130DFD2497F5 && \  
apt-get update && \  
apt-get install -y \  
nodejs=6.10.1-2nodesource1~jessie1 \  
git=1:2.1.4-2.1+deb8u2 \  
curl=7.38.0-4+deb8u5 \  
yarn=0.21.3-1 \  
lsb-release  
  
RUN cd /tmp && git clone https://github.com/wagtail/wagtail.git && \  
cd wagtail && git checkout v1.9  
  
RUN cd /tmp/wagtail && \  
yarn --install && \  
npm run build && \  
rm -r /tmp/wagtail/wagtail/project_template && \  
find /tmp/wagtail/wagtail -name 'static' -exec cp -r {} /tmp/ \; && \  
mv /tmp/static /app  
  
RUN apt-get remove -y --purge nodejs git curl yarn lsb-release && \  
apt-get autoremove -y --purge && \  
rm -r /tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN sed -i -e 's/daemon on;/daemon off;/' /etc/nginx/nginx.conf  
  
RUN echo ".rtl .richtext p, .rtl textarea { text-align: right; direction: rtl;
unicode-bidi: bidi-override; }" >> /app/wagtailadmin/css/core.css  
  
VOLUME /opt/wagtail/sock  
  
RUN rm /etc/nginx/conf.d/*  
COPY nginx.conf /etc/nginx/conf.d/  
  
EXPOSE 80  
WORKDIR /app  

