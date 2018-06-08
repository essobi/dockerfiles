FROM nginx:alpine  
  
RUN apk add --update nodejs && npm i -g yarn  
  
# Fix an alpine bug in nginx logging, check the comment on the answer below:  
# - https://stackoverflow.com/a/42369571/161278  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN mkdir /usr/share/nginx/html/static/  
  
COPY static/package.json static/yarn.lock /usr/share/nginx/html/static/  
RUN cd /usr/share/nginx/html/static/ && yarn install  
RUN chmod a+r -R /usr/share/nginx/html/ \  
&& find /usr/share/nginx/html/ -type d -exec chmod a+x {} \;  
  
ENV ARABIC_JS_VERSION v1.2.1  
RUN mkdir /usr/share/nginx/html/static/arabic-$ARABIC_JS_VERSION  
RUN wget https://cdn.rawgit.com/OmarIthawi/arabic-
mathjax/$ARABIC_JS_VERSION/dist/arabic.js \  
\--output-
document=/usr/share/nginx/html/static/arabic-$ARABIC_JS_VERSION/arabic.js  
  
COPY static/scripts /usr/share/nginx/html/static/scripts  
COPY static/styles /usr/share/nginx/html/static/styles  
  
ENV AMIRI_FONT_VERSION sheen-v0.1.0  
COPY static/fonts /usr/share/nginx/html/static/fonts  
RUN for file in Amiri-Regular.woff2 Amiri-Bold.woff2; do \  
wget
https://github.com/OmarIthawi/amiri/raw/$AMIRI_FONT_VERSION/webfonts/$file \  
\--output-document=/usr/share/nginx/html/static/fonts/amiri/$file; \  
done  
  
RUN cd /usr/share/nginx/html/static && chmod a+r -R scripts/ styles/ fonts/ \  
&& find scripts/ styles/ fonts/ -type d -exec chmod a+x {} \;  
  
COPY index.html /usr/share/nginx/html/index.html  
RUN chmod a+r /usr/share/nginx/html/index.html  

