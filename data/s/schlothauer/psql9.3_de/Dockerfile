FROM postgres:9.3  
RUN localedef -i de_DE -c -f UTF-8 -A /usr/share/locale/locale.alias
de_DE.UTF-8  
ENV LANG de_DE.utf8  
RUN apt-get update && apt-get install -y --force-yes
postgresql-9.3-postgis-2.3  
RUN cd /usr/lib/postgresql/9.3/lib; ln -s postgis-2.3.so postgis-2.2.so  
  
COPY scripts/import.sh /import.sh  
  
ENTRYPOINT ["/import.sh"]  
CMD ["postgres"]  
  

