FROM node:6  
RUN npm i -g raml2html  
RUN npm i -g raml2html-markdown-theme  
RUN npm i -g raml2html-slate-theme  
RUN npm i -g nunjucks@2.5.x  
  
RUN mkdir -p /app  
  
VOLUME /app  
  
CMD case $FORMAT in \  
"md") raml2html --theme 'raml2html-markdown-theme' -i /app/$INPUT -o
/app/$OUTPUT;; \  
"slate") raml2html --theme 'raml2html-slate-theme' -i /app/$INPUT -o
/app/$OUTPUT;; \  
"custom") raml2html --template /app/$TPL -i /app/$INPUT -o /app/$OUTPUT;; \  
*) raml2html -i /app/$INPUT -o /app/$OUTPUT;; \  
esac

