FROM vaca/apk.static  
RUN ["apk.static","--no-cache","--no-progress","add","--upgrade", \  
"luajit", "libsodium-dev", "lua5.1-json4" ]  
  
COPY ["bogonet.lua", "/usr/local/sbin/bogonet"]  
CMD ["bogonet"]  

