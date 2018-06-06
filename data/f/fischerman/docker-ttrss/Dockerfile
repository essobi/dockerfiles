FROM ubuntu:16.04  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
git nginx supervisor php-fpm php-cli php-curl php-gd php-json \  
php-pgsql php-mbstring php-xml php-ldap php-mysql php-mcrypt && apt-get clean
&& rm -rf /var/lib/apt/lists/*  
  
# enable the mcrypt module  
RUN phpenmod mcrypt mbstring  
  
# add ttrss as the only nginx site  
ADD ttrss.nginx.conf /etc/nginx/sites-available/ttrss  
RUN ln -s /etc/nginx/sites-available/ttrss /etc/nginx/sites-enabled/ttrss  
RUN rm /etc/nginx/sites-enabled/default  
  
# install ttrss and patch configuration  
WORKDIR /var/www  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl
--no-install-recommends && rm -rf /var/lib/apt/lists/* \  
&& curl -SL https://git.tt-rss.org/git/tt-rss/archive/17.4.tar.gz | tar xzC
/var/www --strip-components 1 \  
&& apt-get purge -y --auto-remove curl \  
&& chown www-data:www-data -R /var/www  
  
RUN git clone https://github.com/hydrian/TTRSS-Auth-LDAP.git /TTRSS-Auth-LDAP
&& \  
(cd /TTRSS-Auth-LDAP && git reset --hard
c4a207316a2d4e336584b43c6df8ad595e8611fa) && \  
cp -r /TTRSS-Auth-LDAP/plugins/auth_ldap plugins/ && \  
ls -la /var/www/plugins  
RUN cp config.php-dist config.php  
  
RUN (cd /var/www/themes && git clone https://github.com/naeramarth7/clean-
greader && cp clean-greader/wrapper.css clean-greader.css)  
  
RUN mkdir /run/php  
  
# expose only nginx HTTP port  
EXPOSE 80  
# complete path to ttrss  
ENV SELF_URL_PATH http://localhost  
  
# expose default database credentials via ENV in order to ease overwriting  
ENV DB_NAME ttrss  
ENV DB_USER ttrss  
ENV DB_PASS ttrss  
  
# auth method, options are: internal, ldap  
ENV AUTH_METHOD internal  
  
# always re-configure database with current ENV when RUNning container, then
monitor all services  
ADD configure-db.php /configure-db.php  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

