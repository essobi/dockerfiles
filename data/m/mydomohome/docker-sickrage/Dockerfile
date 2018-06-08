FROM python:2.7-wheezy  
  
RUN apt-get update  
RUN apt-get install unrar-free git-core openssl libssl-dev -y  
#RUN addgroup --system sickrage  
#RUN adduser --disabled-password --system --home /var/lib/sickrage --gecos
"SickRage" --ingroup sickrage sickrage  
RUN git clone \--depth 1 https://github.com/SickRage/SickRage.git /sickrage  
#RUN chown sickrage:sickrage /sickrage  
VOLUME /config /downloads /tv  
expose 8081  
ENTRYPOINT python /sickrage/SickBeard.py --datadir=/config  

