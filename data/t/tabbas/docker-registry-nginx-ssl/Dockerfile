FROM containersol/docker-registry-proxy  
  
# modify these  
ENV EMAIL test@example.com  
ENV DOMAIN example.com  
ENV HTPASSWD_USER user  
ENV HTPASSWD_PASS admin  
  
# assume defaults  
ENV REGISTRY_HOST registry  
ENV REGISTRY_PORT 5000  
ENV SERVER_NAME localhost  
  
# set this to "production" in impl to generate working cert  
ENV ENV debug  
  
# allow injection of script to resolve hostname  
#VOLUME /determine_hostname.sh  
# install letsencrypt tool  
RUN apt-get update && \  
apt-get install -y git apache2-utils wget && \  
apt-get clean yoself  
  
# http://askubuntu.com/questions/813859/official-nginx-trusty-ppa-gives-
keyexpired-gpg-error  
RUN wget https://nginx.org/keys/nginx_signing.key -O - | apt-key add -  
  
# install letsencrypt  
RUN (cd ~/ && \  
git clone https://github.com/letsencrypt/letsencrypt && \  
~/letsencrypt/letsencrypt-auto --help)  
  
# runners  
ADD run.sh /run.sh  
ADD determine_hostname.sh /determine_hostname.sh  
RUN chmod +x /run.sh /determine_hostname.sh  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
# TODO: cronjb for auto renewal  
# generate htpassword for basic auth  
#RUN htpasswd -b -c /etc/nginx/.htpasswd ${HTPASSWD_USER} ${HTPASSWD_PASS}  
# entrypoint  
CMD ["/run.sh"]

