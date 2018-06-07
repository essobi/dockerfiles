FROM hunterchung/epiquest-docker  
MAINTAINER Hunter Chung <hchung@zymoresearch.com>  
  
RUN apt-get update && \  
apt-get install -qy \  
mysql-server && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean autoclean && \  
apt-get autoremove -y  
  
ENV DJANGO_SETTINGS_MODULE="EpiQuest_py.migration_settings"  
ENV PYTHONPATH=/usr/share/EpiQuest_py  
ENV DB_HOST_NAME=""  
ENV DB_USERNAME=""  
ENV DB_PASSWORD=""  
CMD migrate.sh  

