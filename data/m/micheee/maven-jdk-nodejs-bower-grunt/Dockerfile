# Pull base image.  
FROM node  
  
# Download latest BaseX release  
ADD http://files.basex.org/releases/BaseX-latest.zip /tmp/BaseX.zip  
ADD saxon.zip /tmp/saxon.zip  
RUN echo "deb http://ftp.de.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get -qq update && \  
apt-get -qq --no-install-recommends install zsh maven zip unzip bzip2
openjdk-8-jre-headless openjdk-8-jdk iceweasel xvfb && \  
npm install --no-color --silent -g bower grunt-cli && \  
unzip /tmp/BaseX.zip -d /opt/ && \  
unzip /tmp/saxon.zip -d /opt/saxon && \  
rm /tmp/BaseX.zip && \  
rm /tmp/saxon.zip && \  
mv /opt/saxon/saxon9he.jar /opt/basex/lib && \  
ln -s /opt/basex/bin/basexhttp /usr/bin/basexhttp && \  
ln -s /opt/basex/bin/basex /usr/bin/basex && \  
sed -i -- 's/Xmx512m/Xmx4096m/g' /opt/basex/bin/basex && \  
sed -i -- 's/Xmx512m/Xmx4096m/g' /opt/basex/bin/basexhttp && \  
wget https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem -O
/tmp/lets-encrypt-x3-cross-signed.pem && \  
keytool -trustcacerts -keystore /etc/ssl/certs/java/cacerts -storepass
changeit -noprompt -importcert -alias isrgrootx3 -file /tmp/lets-
encrypt-x3-cross-signed.pem && \  
wget https://letsencrypt.org/certs/isrgrootx1.pem -O /tmp/isrgrootx1.pem && \  
keytool -trustcacerts -keystore /etc/ssl/certs/java/cacerts -storepass
changeit -noprompt -importcert -alias isrgrootx1 -file /tmp/isrgrootx1.pem  
  
# Define working directory.  
WORKDIR /data  
# Define default command.  
CMD ["bash"]  
  

