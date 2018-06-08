FROM timhaak/tech-maturity-base  
MAINTAINER tim@haak.co  
  
RUN apt-get update && \  
apt-get -qy dist-upgrade && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
RUN git clone https://github.com/timhaak/tech-maturity-api /site/tech-
maturity-api && \  
cd /site/tech-maturity-api/ && \  
npm install && \  
npm run build  
  
RUN git clone https://github.com/timhaak/tech-maturity.git /site/tech-maturity
&& \  
cd /site/tech-maturity/ && \  
npm install && \  
npm run prod  
  
ENV NODE_ENV=production  
  
ADD ./files/nginx_config /site/nginx_config  
ADD ./files/start.sh /start.sh  
ADD ./files/supervisord.conf /supervisord.conf  
  
RUN chmod u+x /start.sh && \  
chown -R nginx: /site/tech-maturity/dist  
  
ENV BASE_URL=""  
WORKDIR /site/  
  
EXPOSE 80 443  
CMD ["/start.sh"]  

