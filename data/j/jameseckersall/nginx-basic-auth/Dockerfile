FROM nginx:alpine  
  
ENV HTPASSWD='foo:$apr1$odHl5EJN$KbxMfo86Qdve2FH4owePn.' \  
FORWARD_PORT=80 \  
FORWARD_HOST=web  
  
WORKDIR /opt  
  
RUN apk add --no-cache gettext  
  
COPY auth.conf auth.htpasswd launch.sh ./  
RUN \  
chown -R root:root /var/cache/nginx && \  
chmod -R 0770 /etc/nginx /var/cache/nginx /var/run && \  
sed -i -E -e '/^user\s+nginx;$/d' /etc/nginx/nginx.conf  
  
CMD ["./launch.sh"]  

