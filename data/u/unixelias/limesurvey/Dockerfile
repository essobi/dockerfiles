FROM tutum/lamp  
  
MAINTAINER Elias Alves <elias.alves@ufvjm.edu.br>  
LABEL Name="Modelo LimeSurvey para implementação no Portal da UFVJM" \  
Version="0.0.1" \  
Architecture="x86_64"  
  
# Localização pt-br  
RUN locale-gen pt_BR \  
&& locale-gen pt_BR.UTF-8 \  
&& dpkg-reconfigure locales \  
&& update-locale LANG=pt_BR.UTF-8  
  
# Atualizando e instalando dependências  
RUN apt-get update \  
&& apt-get upgrade -q -y \  
&& apt-get install -q -y curl php5-gd php5-ldap php5-imap php5-curl sendmail \  
&& apt-get clean \  
&& php5enmod imap \  
&& php5enmod ldap \  
&& php5enmod curl  
  
RUN rm -rf /app  
  
RUN curl -o limesurvey.tar.bz2 -L http://download.limesurvey.org/latest-
stable-release/limesurvey2.72.4+171110.tar.bz2 \  
&& tar -jxf limesurvey.tar.bz2  
  
RUN mv limesurvey app \  
&& mkdir -p /uploadstruct \  
&& chown -R www-data:www-data /app  
  
RUN cp -r /app/upload/* /uploadstruct \  
&& chown -R www-data:www-data /uploadstruct  
  
RUN chown www-data:www-data /var/lib/php5  
  
ADD ldap.php /app/application/config/  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
ADD start.sh /  
RUN chmod +x /start.sh  
  
VOLUME /app/upload  
  
EXPOSE 80 3306  
CMD ["/start.sh"]  

