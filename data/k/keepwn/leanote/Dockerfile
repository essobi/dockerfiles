FROM madnight/docker-alpine-wkhtmltopdf  
MAINTAINER keepwn <keepwn@gmail.com>  
  
RUN apk --update add curl && \  
curl -L https://sourceforge.net/projects/leanote-bin/files/2.5/leanote-linux-
amd64-v2.5.bin.tar.gz/download >> \  
/usr/local/leanote-linux-amd64-v2.5.bin.tar.gz && \  
apk del --purge curl && \  
rm -rf /var/cache/apk/*  
  
COPY fonts/NotoSansCJKsc-Regular.otf /usr/share/fonts/  
  
RUN tar -xzvf /usr/local/leanote-linux-amd64-v2.5.bin.tar.gz -C /usr/local  
EXPOSE 9000  
WORKDIR /usr/local/leanote/bin  
ENTRYPOINT ["sh", "run.sh"]  
  

