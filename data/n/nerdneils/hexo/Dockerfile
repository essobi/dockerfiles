FROM alpine  
MAINTAINER Dengqi <dengqi935@outlook.com>  
RUN apk add --update --no-cache git nodejs  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN npm install -g hexo --save && \  
npm install hexo-generator-feed --save  
RUN mkdir /blog/  
RUN hexo init /blog  
WORKDIR /blog  
RUN npm install  
RUN git clone https://github.com/nerdneilsfield/Hexo-theme-Teas themes/teas  
RUN rm _config.yml  
ADD _config.yml /blog/  
RUN echo "hello"  
RUN hexo new page "about"  
RUN hexo new page "tags"  
RUN hexo new page categories  
RUN rm -f /blog/source/tags/index.md /blog/source/categories/index.md  
ADD favicon.ico /post/source/  
ADD tags.md /blog/source/tags/index.md  
ADD cat.md /blog/source/categories/index.md  
ADD 404.html /blog/source/  
# RUN rm -r /blog/source/_post  
CMD ["hexo", "generate","--watch"]  
#hexo <generate></generate>  

