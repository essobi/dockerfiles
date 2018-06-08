FROM alpine  
  
# 不添加writev配置的话挂载目录修改文件后访问的还是旧的数据(我的mac是如此,linux无此情况,windows没测试过)  
RUN apk add --update lighttpd && echo server.network-backend = \"writev\" >>
/etc/lighttpd/lighttpd.conf && rm -rf /var/cache/apk/*  
  
EXPOSE 80  
VOLUME /var/www/localhost/htdocs  
  
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

