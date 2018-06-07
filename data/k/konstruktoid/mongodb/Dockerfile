FROM konstruktoid/debian:stretch  
  
COPY ./files/ /etc/mongod/  
  
ENV GPGKEY 58712A2291FA4AD5 3DAB71713396F72B 4B7C549A058F8B6B  
ENV MONGOVER development  
  
RUN \  
groupadd -r mongodb && \  
useradd -r -g mongodb mongodb && \  
apt-get -y install dirmngr gnupg --no-install-recommends && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv $GPGKEY && \  
echo "deb http://repo.mongodb.org/apt/debian "$(. /etc/os-release && \  
echo $VERSION | sed 's/[^a-z]*//g')"/mongodb-org/$MONGOVER main" | \  
tee /etc/apt/sources.list.d/mongodb-org-$MONGOVER.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y mongodb-org ca-certificates --no-install-recommends && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* \  
/usr/share/doc /usr/share/doc-base \  
/usr/share/man /usr/share/locale /usr/share/zoneinfo && \  
mkdir -p /data/db && \  
chown -R mongodb:mongodb /data/db /etc/mongod && \  
chmod a+x /etc/mongod/*.sh && \  
chmod 400 /etc/mongod/mongodb.keyfile && \  
/etc/mongod/mongocert.sh  
  
VOLUME /data/db  
EXPOSE 27017  
ENTRYPOINT ["/etc/mongod/mongostart.sh"]  
CMD [""]  

