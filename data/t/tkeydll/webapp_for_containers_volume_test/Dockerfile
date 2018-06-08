# 4の構成で VOLLUME 指定するとどうなるか（パスを変更）  
FROM nginx:alpine  
  
RUN mkdir -p /home/LogFiles \  
&& mkdir -p /home/site/wwwroot  
  
RUN rm -rf /usr/share/nginx/html \  
&& ln -s /home/site/wwwroot /usr/share/nginx/html  
  
COPY ./site/index.html /home/site/wwwroot/index.html  
COPY ./site /home/hoge  
  
VOLUME ["/home/hoge/subdir"]  

