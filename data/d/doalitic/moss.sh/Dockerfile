FROM doalitic/nginx:1.8  
  
MAINTAINER "The Doalitic Team" <devops@doalitic.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends curl \  
git \  
build-essential \  
make \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y --no-install-recommends nodejs \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN wget
https://github.com/spf13/hugo/releases/download/v0.19/hugo_0.19-64bit.deb \  
&& dpkg -i hugo_0.19-64bit.deb  
  
ADD ./app /var/www  
RUN chown -R nginx:nginx /var/www  
  
WORKDIR /var/www/  
  
RUN hugo -s /var/www/src/blog -d /var/www/build/blog \  
&& hugo -s /var/www/src/blog-es -d /var/www/build/es/blog  
  
RUN npm install && \  
node_modules/.bin/gulp build && \  
mv build public && \  
rm -rf src && \  
rm -rf node_modules && \  
rm gulpfile.js && \  
rm package.json  
  
CMD [ "dockerize", \  
"-template",
"/etc/container/templates/server.key.tpl:/etc/ssl/private/server.key", \  
"-template",
"/etc/container/templates/server.crt.tpl:/etc/ssl/private/server.crt", \  
"-template", "/etc/container/templates/nginx.conf.tpl:/etc/nginx/nginx.conf",
\  
"-template", "/etc/container/templates/nginx.conf.tpl:/etc/nginx/nginx.conf",
\  
"-template",
"/var/www/public/assets/js/vars.tpl.js:/var/www/public/assets/js/vars.js", \  
"nginx", "-g", "daemon off;" ]

