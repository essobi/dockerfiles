FROM mophos/mmis-nginx  
  
LABEL maintainer="Satit Rianpit <rianpit@gmail.com>"  
  
WORKDIR /home/mmis  
  
RUN npm i npm@latest -g  
  
RUN npm i -g pm2  
  
RUN git clone https://github.com/mophos/mmis-frontend-dist \  
&& git clone https://github.com/mophos/mmis-inventory-backend \  
&& cd mmis-inventory-backend \  
&& mv views/css.pug.txt views/css.pug \  
&& npm i && npm run build && cd .. \  
&& git clone https://github.com/mophos/mmis-purchase-backend \  
&& cd mmis-purchase-backend \  
&& mv views/css.pug.txt views/css.pug \  
&& npm i && npm run build && cd .. \  
&& git clone https://github.com/mophos/mmis-material-backend \  
&& cd mmis-material-backend \  
&& mv views/css.pug.txt views/css.pug \  
&& npm i && npm run build && cd .. \  
&& git clone https://github.com/mophos/mmis-management-backend \  
&& cd mmis-management-backend \  
&& mv views/css.pug.txt views/css.pug \  
&& npm i && npm run build && cd .. \  
&& git clone https://github.com/mophos/mmis-portal-backend \  
&& cd mmis-portal-backend \  
&& mv views/css.pug.txt views/css.pug \  
&& npm i && npm run build && cd .. \  
&& git clone https://github.com/mophos/mmis-contract-backend \  
&& cd mmis-contract-backend \  
&& mv views/css.pug.txt views/css.pug \  
&& npm i && npm run build && cd .. \  
&& git clone https://github.com/mophos/mmis-planning-backend \  
&& cd mmis-planning-backend \  
&& mv views/css.pug.txt views/css.pug \  
&& npm i && npm run build && cd .. \  
&& git clone https://github.com/mophos/mmis-documents-management \  
&& cd mmis-documents-management \  
&& npm i && npm run build && cd ..  
  
COPY ./server-script/ .  
  
RUN npm init -y && npm i express  
  
COPY ./config/nginx.conf /etc/nginx  
  
COPY ./config/process.json .  
  
CMD /usr/sbin/nginx && /usr/bin/pm2-runtime process.json  
  
EXPOSE 80

