FROM postgres:9.3  
RUN cat /usr/share/i18n/SUPPORTED | grep sv_SE > /etc/locale.gen && locale-gen  
RUN apt-get update && apt-get install postgresql-contrib-9.3 -yqq  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

