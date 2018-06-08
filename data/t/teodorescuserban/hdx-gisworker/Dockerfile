FROM teodorescuserban/hdx-gislayer:latest  
  
MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com  
  
RUN rm -rf /etc/service/gislayer && \  
mkdir -p /etc/service/gisworker && \  
echo "*/10 * * * * /srv/clean_up_folder.py" > /var/spool/cron/crontabs/root  
COPY run /etc/service/gisworker/  
RUN chmod +x /etc/service/gisworker/run  
COPY clean_up_folder.py /srv/  

