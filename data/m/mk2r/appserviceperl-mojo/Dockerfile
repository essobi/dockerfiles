FROM httpd:2.4  
COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf  
  
# establising symlinks  
# /usr/local/apache2/htdocs -> /home/site/wwwroot and  
# /usr/local/apache2/logs -> /home/LogFiles  
RUN rm -f /usr/local/apache2/logs/* \  
&& chmod 777 /usr/local/apache2/logs \  
&& rm -rf /usr/local/apache2/htdocs \  
&& rm -rf /usr/local/apache2/logs \  
&& mkdir -p /home/site/wwwroot \  
&& mkdir -p /home/LogFiles \  
&& chown -R root:www-data /home \  
&& ln -s /home/site/wwwroot /usr/local/apache2/htdocs \  
&& ln -s /home/LogFiles /usr/local/apache2/logs  
  
# installing perl again as cpanm fails with default installation. Could be env
issue  
RUN apt-get update \  
&& apt-get install make \  
&& apt-get install -y perl  
  
#creating a /home/cpan directory for temporary use  
RUN mkdir -p /home/cpan  
  
# copying cpanfile to /home/cpan/cpanfile. this file has required perl
dependencies  
COPY ./cpanfile /home/cpan/cpanfile  
  
# installing cpanm inside /home/cpan to insall modules listed in cpanfile  
RUN apt-get install -y curl \  
&& cd /home/cpan \  
&& curl -LO http://xrl.us/cpanm \  
&& apt-get install -y libhtml-parser-perl \  
&& perl cpanm --force --installdeps .  
  
# deleting /home/cpan folder as we don't need it anymore  
RUN rm -rf /home/cpan  

