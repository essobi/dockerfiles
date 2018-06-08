FROM masm/archlinux  
MAINTAINER Marco Monteiro <marco@neniu.org>  
  
ENTRYPOINT ["/bin/sh", "/start.sh"]  
EXPOSE 5985  
VOLUME /opt/couchdb-lucene/indexes  
  
RUN pacman -Sq couchdb-lucene --needed --noconfirm --noprogressbar && \  
yes | pacman -Sqcc && \  
rm -rf /usr/share/man/* && \  
sed -e 's/^host=localhost$/host=0.0.0.0/' -i /opt/couchdb-lucene/conf/couchdb-
lucene.ini  
  
COPY start.sh /start.sh  

