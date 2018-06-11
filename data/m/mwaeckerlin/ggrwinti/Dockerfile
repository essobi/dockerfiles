FROM mwaeckerlin/nextcloud  
MAINTAINER mwaeckerlin  
  
ENV APPS "ggrwinti calendar contacts groupfolders"  
ENV DEBUG "1"  
RUN apt-get update -y && apt-get install -y ggrwinti && mv ${APPSDIR}/ggrwinti
/${APPSDIR}.original/  
  
ADD cronjob.sh /etc/cron.daily/update-db  
ADD start-ggrwinti.sh /start-ggrwinti.sh  
  
CMD /start-ggrwinti.sh

