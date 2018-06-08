FROM ubuntu:14.04  
MAINTAINER fabian.hartmann@bluewin.ch  
  
# Enviroment Variables for Datacontainer and Restore from Backup.  
ENV VIRTUAL_HOST=asus.example.com  
ENV REPOSADOURL=asus.example.com  
ENV MARGARITAURL=masus.example.com  
  
# Installs nessesary binarys.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
# echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install libapache2-mod-wsgi git python-setuptools python curl
python-pip apache2 cron nano screen supervisor && \  
rm -rf /var/lib/apt/lists/* && \  
easy_install flask && \  
easy_install simplejson  
  
# installs reposado and margarita  
RUN mkdir /usr/local/asus && \  
cd /usr/local/asus && \  
git clone https://github.com/wdas/reposado.git && \  
git clone https://github.com/jessepeterson/margarita.git  
# enables apaches rewrite module  
RUN a2enmod rewrite  
  
# adds all the nessesary configuration Files.  
ADD ./init.sh /srv/  
ADD CONF/preferences.plist /usr/local/asus/reposado/code/  
ADD ports.conf /etc/apache2/ports.conf  
ADD margarita.conf /etc/apache2/sites-enabled/margarita.conf  
ADD margarita.wsgi /usr/local/asus/margarita/margarita.wsgi  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN ln -s /usr/local/asus/reposado/code/preferences.plist
/usr/local/asus/margarita  
RUN ln -s /usr/local/asus/reposado/code/reposadolib
/usr/local/asus/margarita/reposadolib  
  
ENV HOME /root  
EXPOSE 80  
WORKDIR /srv/MMServiceData/MM-REPOSADO  
  
VOLUME ["/srv/MMServiceData/MM-REPOSADO"]  
  
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf  

