FROM klaemo/couchdb:1.6  
MAINTAINER Antoine GIRARD <antoine.girard@sapk.fr>  
  
ADD scripts /scripts  
  
#RUN apt-get update -y -qq && apt-get install -y --no-install-recommends
netcat pwgen git nodejs \  
# && npm install -g gulp bower-installer && ln -s /usr/bin/nodejs
/usr/bin/node \  
# && apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN apt-get update -y -qq && apt-get install -y --no-install-recommends netcat
pwgen git \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN sed -e 's/^database_dir = .*$/database_dir = \/data/' -i
/usr/local/etc/couchdb/default.ini && \  
sed -e 's/^view_index_dir = .*$/view_index_dir = \/data/' -i
/usr/local/etc/couchdb/default.ini && \  
echo '_default = [{db_fragmentation, "70%"}, {view_fragmentation, "60%"}]' >>
/usr/local/etc/couchdb/default.ini && \  
chmod +x /scripts/*.sh && touch /.firstrun  
#[compactions] is at the end of file so simply append  
# Command to run  
ENTRYPOINT ["/scripts/run.sh"]  
#CMD [""]  
# Expose listen port  
EXPOSE 5984  
# Expose our data, logs and configuration volumes  
VOLUME ["/data"]  

