FROM alpine:edge  
  
RUN apk add --update --no-cache nginx curl  
RUN mkdir /usr/share/nginx && mkdir /usr/share/nginx/html && cd /root && curl
-sL https://github.com/toyorg/TI/archive/master.tar.gz | tar xz && cp -r TI-
master/docs/* /usr/share/nginx/html && rm -rf TI-master/ master.tar.gz  
  
#RUN apk add --update --no-cache nginx  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf  
  
COPY check.sh /root/check.sh  
RUN touch /root/hash && echo '.' > /root/hash && chmod +x /root/check.sh &&
echo "*/1 * * * * /bin/sh -c /root/check.sh" >> /etc/crontabs/root  
  
#VOLUME ["/usr/share/nginx/html"]  
EXPOSE 80  
#EXPOSE 443  
CMD nginx -g "daemon off;"  

