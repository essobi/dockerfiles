FROM node:alpine  
  
MAINTAINER Wang Qun, <qun.wang@live.cn>  
  
WORKDIR /Hexo  
  
RUN \  
apk add --no-cache git openssh-client \  
&& npm install hexo-cli -g \  
&& hexo init . \  
&& npm install \  
&& npm install hexo-generator-sitemap --save \  
&& npm install hexo-generator-feed --save \  
&& npm install hexo-generator-searchdb --save \  
&& npm install hexo-deployer-git --save \  
&& npm install gulp -g \  
&& npm install gulp --save \  
&& npm install gulp-inline --save \  
&& npm install gulp-uglify --save \  
&& npm install gulp-clean-css --save \  
&& npm install gulp-htmlmin --save \  
&& npm install pump --save  
  
VOLUME ["/Hexo/source", "/Hexo/themes", "/root/.ssh"]  
  
EXPOSE 80  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY gulpfile.js /Hexo/gulpfile.js  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ['/bin/bash']  

