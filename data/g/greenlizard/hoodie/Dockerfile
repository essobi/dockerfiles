  
FROM greenlizard/nodejs  
  
MAINTAINER GreenLizard Labs <gabriel@greenlizard.com.br>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
nginx \  
monit \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install -g hoodie-cli  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Add an xroot user because hoodie doesn't like being root  
RUN adduser --disabled-password --gecos "" xroot && \  
echo "xroot ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# Expose the port  
ENV WWW 6001  
ENV ADMIN 6002  
ENV COUCH 5984  
ENV HOME /home/xroot  
  
ENV LANG en_US.UTF-8  
RUN mkdir /src && chown xroot:xroot /src  
  
VOLUME /src  
WORKDIR /src  
EXPOSE $WWW $ADMIN  
  
ENV HOODIE_BIND_ADDRESS 0.0.0.0  
ENV HOODIE_ADMIN_USER admin  
ENV HOODIE_ADMIN_PASS admin  
ENV COUCH_URL http://couchdb:$COUCH  
  
  
#hoodie soft nofile 768  
#hoodie hard nofile 1024  
#  
## Configure Couchdb  
#RUN sed -e 's/^delayed_commits = .*$/delayed_commits = false/' -i
/usr/local/etc/couchdb/default.ini  
#RUN sed -e 's/^max_dbs_open = .*$/max_dbs_open = 1024/' -i
/usr/local/etc/couchdb/default.ini  
#RUN sed -e 's/^timeout = .*$/timeout = 1209600/' -i
/usr/local/etc/couchdb/default.ini  
COPY ./docker-entrypoint.sh /entrypoint.sh  
  
#RUN chmod +x /entrypoint.sh  
#RUN chown xroot:xroot /entrypoint.sh  
#USER xroot  
ONBUILD RUN npm install  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [ "hoodie", "start", "--noBrowser", "--custon-ports", "$WWW,$ADMIN" ]  
#ENTRYPOINT [ "hoodie" ]  

