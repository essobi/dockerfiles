FROM node:8.1  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
LABEL MAINTAINER 'Kazumichi Yamamoto <yamamoto.febc@gmail.com>'  
  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
RUN npm install -g --no-cache textlint \  
textlint-filter-rule-whitelist \  
textlint-filter-rule-comments \  
textlint-rule-common-misspellings \  
textlint-rule-preset-ja-technical-writing \  
textlint-rule-preset-jtf-style  
  
WORKDIR /workdir  
ENTRYPOINT ["textlint"]  

