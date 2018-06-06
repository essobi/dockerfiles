FROM rkrahl/glassfish:payara-4.1  
  
USER root  
  
RUN zypper --non-interactive install \  
python-base \  
python-xml && \  
mkdir -p /srv/ids/storage/data \  
/srv/ids/storage/archive \  
/srv/ids/storage/cache && \  
chown -R glassfish:glassfish /srv/ids/storage && \  
chmod 0700 /srv/ids/storage/data \  
/srv/ids/storage/archive \  
/srv/ids/storage/cache  
  
USER glassfish  
  
RUN mkdir -p $GLASSFISH_HOME/apps && \  
tmpfile=`mktemp` && \  
for dist in \  
https://repo.icatproject.org/repo/org/icatproject/authn.anon/2.0.0/authn.anon-2.0.0-distro.zip
\  
https://repo.icatproject.org/repo/org/icatproject/authn.db/2.0.0/authn.db-2.0.0-distro.zip
\  
https://repo.icatproject.org/repo/org/icatproject/authn.ldap/2.0.0/authn.ldap-2.0.0-distro.zip
\  
https://repo.icatproject.org/repo/org/icatproject/authn.simple/2.0.0/authn.simple-2.0.0-distro.zip
\  
https://repo.icatproject.org/repo/org/icatproject/icat.server/4.9.1/icat.server-4.9.1-distro.zip
\  
https://repo.icatproject.org/repo/org/icatproject/icat.lucene/1.1.0/icat.lucene-1.1.0-distro.zip
\  
https://repo.icatproject.org/repo/org/icatproject/ids.storage_file/1.4.1/ids.storage_file-1.4.1-distro.zip
\  
https://repo.icatproject.org/repo/org/icatproject/ids.server/1.9.0/ids.server-1.9.0-distro.zip
\  
https://repo.icatproject.org/repo/org/icatproject/topcat/2.3.6/topcat-2.3.6-distro.zip;
\  
do \  
curl --silent --show-error --location --output $tmpfile $dist && \  
unzip -q -d $GLASSFISH_HOME/apps $tmpfile; \  
done && \  
rm -rf $tmpfile && \  
chmod -R go-w $GLASSFISH_HOME/apps && \  
mkdir -p $GLASSFISH_HOME/etc/icat  
  
COPY setup-icat.sh /etc/glassfish.d/10-setup-icat.sh  

