FROM nginx:alpine  
RUN apk add --no-cache gettext  
ENV TOP_MSG="This page is taking way too long to load."  
ENV BOTTOM_MSG="Sorry about that. Please try refreshing and contact us if the
problem persists."  
COPY ./index.html.tpl /usr/share/nginx/html/  
CMD envsubst < /usr/share/nginx/html/index.html.tpl >
usr/share/nginx/html/index.html; exec nginx -g "daemon off;"  

