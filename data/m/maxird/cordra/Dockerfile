FROM maxird/java:7-8  
  
RUN export VERSION=1.0.7 && \  
cd /opt && \  
wget -q -O - https://www.cordra.org/unconfiguredInstanceDownload | python -c
"import
zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall('.')"
&& \  
ln -s `/bin/ls -d cordra-*` cordra && \  
chmod u+x /opt/cordra/startup && \  
chmod u+x /opt/cordra/shutdown && \  
chmod u+x /opt/cordra/sw/bin/do-server && \  
echo '/opt/cordra/sw/bin/do-server $*' > /opt/cordra/run && \  
chmod u+x /opt/cordra/run && \  
mkdir -p /opt/cordra/config && \  
touch /opt/cordra/config/password.dct && \  
touch /opt/cordra/config/config.dct && \  
touch /opt/cordra/config/privatekey && \  
touch /opt/cordra/config/publickey && \  
cd /opt/cordra/data && \  
ln -sf ../config/password.dct password.dct && \  
ln -sf ../config/config.dct config.dct && \  
ln -sf ../config/privatekey privatekey && \  
ln -sf ../config/publickey publickey && \  
cd /opt/cordra/config && \  
rm -f password.dct config.dct privatekey publickey  
  
ADD dev-init /opt/cordra/dev-init  
ADD startup /opt/cordra/startup  
  
EXPOSE 8080  
  
VOLUME /opt/cordra/data  
VOLUME /opt/cordra/config  
  
CMD ["/opt/cordra/startup"]  

