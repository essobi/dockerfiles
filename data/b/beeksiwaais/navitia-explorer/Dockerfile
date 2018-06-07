FROM nginx:stable-alpine  
  
EXPOSE 80  
COPY . /usr/share/nginx/html  
  
ENV MAIN_HOST=api.navitia.io  
ENV NAVITIA=http://api.navitia.io/v1/  
ENV TYR=http://tyr.navitia.io/v0/  
ENV KEY="your_navitia_io_key"  
ENV COVERAGE="fr-idf"  
CMD /bin/bash -c "envsubst < /usr/share/nginx/html/params.tmpl >
/usr/share/nginx/html/params.json && nginx -g 'daemon off;'"  

