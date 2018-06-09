# A partir d'une image ubuntu en version 16.04  
FROM ubuntu:16.04  
# Installer tous les paquets nécessaires :  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends apt-utils \  
&& apt-get install -y nginx \  
&& apt-get install -y php-fpm php7.0-mysql \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& apt-get update  
  
# Placer les configurations des sites  
COPY default /etc/nginx/sites-available/  
COPY wt1.ephec-ti.be /etc/nginx/sites-available/  
COPY b2b.wt1.ephec-ti.be /etc/nginx/sites-available/  
COPY intranet.wt1.ephec-ti.be /etc/nginx/sites-available/  
  
# Copier les configurations dans sites-enabled  
RUN ln -s /etc/nginx/sites-available/wt1.ephec-ti.be /etc/nginx/sites-enabled/  
RUN ln -s /etc/nginx/sites-available/b2b.wt1.ephec-ti.be /etc/nginx/sites-
enabled/  
RUN ln -s /etc/nginx/sites-available/intranet.wt1.ephec-ti.be
/etc/nginx/sites-enabled/  
  
# Modifier la configuration par défaut de PHP7.0 en passant le paramètres
cgi.fix_pathinfo à 0  
RUN sed -i -e 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g'
/etc/php/7.0/fpm/php.ini  
  
# Créer les répertoires pour les certificats HTTPS  
RUN mkdir -p /etc/letsencrypt/b2b.wt1.ephec-ti.be  
RUN mkdir -p /etc/letsencrypt/wt1.ephec-ti.be  
  
# Copier les certificats HTTPS du site B2B  
COPY b2b-certificate.crt /etc/letsencrypt/b2b.wt1.ephec-ti.be/  
COPY b2b-certificate.key /etc/letsencrypt/b2b.wt1.ephec-ti.be/  
  
# Copier les certificats HTTPS du site wt1  
COPY wt1-certificate.crt /etc/letsencrypt/wt1.ephec-ti.be/  
COPY wt1-certificate.key /etc/letsencrypt/wt1.ephec-ti.be/  
  
# Exposer les ports  
EXPOSE 80 443  
# Lancer PHP et nginx en mode démon  
CMD service php7.0-fpm start && nginx -g "daemon off;"  
  

