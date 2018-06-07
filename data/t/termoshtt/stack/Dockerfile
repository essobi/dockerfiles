FROM fpco/stack-build:lts-6.15  
MAINTAINER termoshtt <toshiki.teramura@gmail.com>  
COPY stack.yaml /root/.stack/global-project/  
RUN stack install persistent persistent-sqlite persistent-template scotty lens
wai-middleware-static  

