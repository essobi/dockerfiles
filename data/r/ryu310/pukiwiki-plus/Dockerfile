FROM php:7.2.2-apache  
  
MAINTAINER Ryu Sato <ryu@weseek.co.jp>  
  
# Variable environment value  
ENV SUBDIR "/"  
ENV WITHOUT_APACHEGUI ""  
# Const environment value  
ARG PUKIWIKIPLUS_INITDIR="/usr/src/pukiwiki_plus"  
ARG PUKIWIKIPLUS_PLUGINDIR="${PUKIWIKIPLUS_INITDIR}/plugin"  
# Install ApacheGUI  
## It is needed to make directory "/usr/share/man/man1"  
## cf. https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199  
RUN mkdir -p /usr/share/man/man1 \  
&& apt-get update && apt-get install -y \  
tar wget openjdk-8-jre \  
&& rm -rf /var/lib/apt/lists/*  
RUN cd ~ \  
&& wget https://netcologne.dl.sourceforge.net/project/apachegui/1.11-Linux-
Solaris-Mac/ApacheGUI-1.11.0.tar.gz -O ApacheGUI.tar.gz \  
&& tar zxvf ApacheGUI.tar.gz \  
&& mv ApacheGUI /opt  
ENV APACHEGUI_HOME "/opt/ApacheGUI"  
# Install Pukiwiki  
RUN cd /  
RUN apt-get update && apt-get install -y \  
git \  
&& rm -rf /var/lib/apt/lists/*  
RUN git clone git://git.pf.osdn.net/gitroot/n/ni/night1ynx/pukiwiki_plus.git
${PUKIWIKIPLUS_INITDIR} \  
&& rm -rf ${PUKIWIKIPLUS_INITDIR}/.git  
  
# Install pukiwiki-plus plugin  
## ls2_1  
## ref: http://pukiwiki.sonots.com/?Old%2FPlugin%2Fls2_1.inc.php  
ARG PUKIWIKIPLUS_PLUGIN_LS2_1_VER="27"  
RUN cd ${PUKIWIKIPLUS_PLUGINDIR} \  
&& curl -o ls2_1.inc.php -SL
"http://pukiwiki.sonots.com/?plugin=attach&refer=Old%2FPlugin%2Fls2_1.inc.php&openfile=ls2_1.inc.php.${PUKIWIKIPLUS_PLUGIN_LS2_1_VER}"  
  
# Set permissions of pukiwiki  
RUN cd ${PUKIWIKIPLUS_INITDIR} \  
&& chown -R www-data:www-data ${PUKIWIKIPLUS_INITDIR}  
  
# Prepare apache user for sudoers  
RUN apt-get update && apt-get install -y \  
sudo \  
&& rm -rf /var/lib/apt/lists/*  
RUN echo "${APACHE_RUN_USER:-www-data} ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
VOLUME /var/www/html  
VOLUME /etc/apache2  
VOLUME /opt/ApacheGUI/tomcat/db  
VOLUME /usr/local/etc/php  
  
COPY scripts/app-entrypoint.sh /  
RUN chmod +x /app-entrypoint.sh  
USER ${APACHE_RUN_USER:-www-data}  
ENTRYPOINT [ "sudo", "-E", "/app-entrypoint.sh" ]  
CMD ["sudo", "-E", "apache2-foreground"]  

