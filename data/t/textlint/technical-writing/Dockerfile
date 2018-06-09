FROM node:latest  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
ENV TEXTLINT_VERSION=7.0.2  
RUN npm install -g textlint@${TEXTLINT_VERSION} \  
&& npm install -g \  
textlint-rule-preset-ja-technical-writing  
WORKDIR /work  
ADD .textlintrc /  
  
ENTRYPOINT ["textlint" , "--config" , "/.textlintrc"]  
CMD ["-h"]  

