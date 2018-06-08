FROM nginx  
RUN apt-get update && apt-get install -y wget zip && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
COPY ./static /usr/share/nginx/html  
WORKDIR /usr/share/nginx/html  
RUN wget
https://bitbucket.org/__freeman__/rekod_user_layers_qgis/get/default.zip &&\  
unzip default.zip &&\  
mv *rekod_user_layers_qgis* rekod_user_layers &&\  
zip -r rekod_user_layers rekod_user_layers &&\  
rm default.zip && rm -r rekod_user_layers  

