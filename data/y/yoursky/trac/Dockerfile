FROM ruimashita/pip  
  
LABEL maintainer "skyisno.1@gmail.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN pip install --no-cache-dir trac \  
psycopg2 \  
pwgen  
  
COPY setup_trac_config.sh /.setup_trac_config.sh  
COPY setup_trac.sh /.setup_trac.sh  
COPY run.sh /run.sh  
COPY trac_logo.png /var/www/trac_logo.png  
  
COPY set_trac_user_password.py /usr/local/bin/  
RUN chmod 755 /usr/local/bin/set_trac_user_password.py  
  
EXPOSE 80  
CMD ["/run.sh"]  

