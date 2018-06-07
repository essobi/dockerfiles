FROM nginx:stable  
LABEL maintainer "And Grin <a@grin.ly>"  
  
# update, install certbot and stuff, then clean up  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list &&\  
apt-get -yq update && \  
apt-get -yq --no-install-recommends install certbot -t jessie-backports && \  
apt-get -yq --no-install-recommends install dnsutils python-ndg-httpsclient &&
\  
apt-get clean && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/archive/* /var/lib/apt/lists/*  
  
RUN openssl dhparam -out /etc/nginx/dhparams.pem 2048  
  
# copy the context  
COPY ./container/root /  
  
VOLUME ["/etc/letsencrypt"]  
  
RUN chmod u+x /app/recert.sh &&\  
chmod u+x /app/startup.sh  
  
CMD ["bash", "-C", "/app/startup.sh"]  

