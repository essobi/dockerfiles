# 2014-11-14  
# Peter.Kutschera@ait.ac.at  
# docker build -t peterkutschera/crisma-model_wps resourceModel_WPS  
# docker run -P -d --env
MODEL_ENDPOINT='http://localhost/Startup/startup.aspx' peterkutschera/crisma-
resource_model_wps  
FROM debian:7.7  
MAINTAINER Peter.Kutschera@ait.ac.at  
  
RUN apt-get update && apt-get install -y apache2 python python-magic python-
requests && apt-get clean  
  
# If pythoin-requests is to olg get the newer version instead:  
# RUN apt-get install python-pip  
# RUN pip install requests  
COPY var/www /var/www/  
COPY usr/local/wps /usr/local/wps/  
ADD pywps-3.2.1.tgz /usr/local/  
  
RUN chmod 777 /usr/local/pywps-3.2.1/pywps/Templates/1_0_0  
  
COPY usr/lib/* /usr/lib/cgi-bin/  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# RUN /bin/ln -sf ../sites-available/default-ssl /etc/apache2/sites-
enabled/001-default-ssl  
# RUN /bin/ln -sf ../mods-available/ssl.conf /etc/apache2/mods-enabled/  
# RUN /bin/ln -sf ../mods-available/ssl.load /etc/apache2/mods-enabled/  
EXPOSE 80  
# EXPOSE 443  
ENV MODEL_ENDPOINT http://localhost/resourcemodel/Startup/startup.aspx  
  
WORKDIR /root  
# COPY root/bin/runAll.sh /root/bin/runAll.sh  
# RUN chmod +x /root/bin/*  
# CMD ["/root/bin/runAll.sh"]  
CMD perl -i.bak -p -e "s{baseUrl\s*=.*}{baseUrl = '${MODEL_ENDPOINT}'}"
/usr/local/wps/processes/AgentsResourceModel.py && \  
touch ${APACHE_LOG_DIR}/access.log touch ${APACHE_LOG_DIR}/error.log && \  
/etc/init.d/apache2 start && \  
tail -f ${APACHE_LOG_DIR}/access.log ${APACHE_LOG_DIR}/error.log  

