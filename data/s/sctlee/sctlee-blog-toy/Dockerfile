FROM simplyintricate/hexo  
MAINTAINER Secret Lee "sctlee221@gmail.com"  
COPY _config.yml /usr/share/nginx/html/_config.yml  
  
COPY themes /usr/share/nginx/html/themes  
COPY _theme_config.yml /usr/share/nginx/html/themes/apollo/_config.yml  
  
RUN rm -f /usr/share/nginx/html/source/_posts/*  
COPY source /usr/share/nginx/html/source  
  
RUN npm install --save hexo-renderer-jade hexo-generator-feed hexo-generator-
sitemap hexo-browsersync hexo-generator-archive  
RUN hexo generate  
  
ENV DAOVOICE_API_ID=1  
COPY dao_script /usr/share/nginx/html/public/dao_script  
  
CMD /usr/share/nginx/html/public/dao_script/daovoice.sh  

