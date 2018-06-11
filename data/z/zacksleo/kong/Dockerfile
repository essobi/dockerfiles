FROM kong:0.13  
#ENTRYPOINT ping 127.0.0.1  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
CMD ["/usr/local/openresty/nginx/sbin/nginx", "-c",
"/usr/local/kong/nginx.conf", "-p", "/usr/local/kong/"]

