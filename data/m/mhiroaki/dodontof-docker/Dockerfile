FROM ubuntu  
MAINTAINER mhiroaki  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends wget unzip mysql-server ruby
ruby-mysql ruby-msgpack apache2 \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* \  
&& install -d -o mysql -g mysql -m 755 /var/run/mysqld \  
&& ln -s /var/run/mysqld/mysqld.sock /tmp/mysql.sock \  
&& ln -s ../mods-available/cgi.load /etc/apache2/mods-enabled \  
&& install -d /var/lock/apache2 \  
&& install -d /var/run/apache2 \  
&& echo 'ServerName dodontof' > /etc/apache2/conf-enabled/servername.conf  
  
ADD mysqld.cnf /etc/mysql/mysql.conf.d/  
ADD dodontof.conf /etc/apache2/sites-enabled/  
ADD run.sh /  
  
CMD [ "/run.sh" ]  
EXPOSE 80  
VOLUME /var/lib/mysql  
  
ARG DODONTOF_VERSION=Ver.1.48.18  
ADD sha256sum /var/tmp  
  
RUN cd /var/tmp/ \  
&& INFO=`grep $DODONTOF_VERSION sha256sum` \  
&& URI=`echo "$INFO" | awk '{print $3}'` \  
&& SHA256=`echo "$INFO" | awk '{print $1}'` \  
&& wget -O /var/tmp/DodontoF.zip "${URI}" \  
&& echo "$SHA256 DodontoF.zip" | sha256sum -c \  
&& unzip DodontoF.zip \  
&& rm -f /var/tmp/DodontoF.zip \  
&& rm -f /var/www/html/index.html \  
&& mv /var/tmp/DodontoF_WebSet/public_html/DodontoF/* /var/www/html/ \  
&& mv /var/tmp/DodontoF_WebSet/saveData /var/www/ \  
&& mv /var/tmp/DodontoF_WebSet/public_html/imageUploadSpace/ /var/www/html/ \  
&& find /var/www/saveData -type d | xargs chmod 777 \  
&& find /var/www/saveData -type f | xargs chmod 666 \  
&& cd /var/www/html/ \  
&& sed -i -e '/^#!/i #!/usr/bin/ruby' DodontoFServer.rb \  
&& sed -i -e '/DodontoFServer\\.rb/i if ($0 == __FILE__)' \  
-e '/DodontoFServer\\.rb/a end' \  
DodontoFServerMySql.rb \  
&& sed -i -e '/^#!/i #!/usr/bin/ruby' DodontoFServerMySqlKai.rb \  
&& chmod +x DodontoFServer.rb DodontoFServerMySqlKai.rb \  
&& chmod 666 log.txt log.txt.0  
COPY config.rb /var/www/html/src_ruby/config.rb.in  

