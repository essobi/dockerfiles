FROM maven:3.3  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
daemontools \  
inotify-tools \  
moreutils \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
python-pkg-resources \  
python-requests \  
python-setuptools \  
&& \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
python-pip \  
&& \  
pip install hchk \  
&& \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y --auto-remove --purge purge \  
patch \  
python-pip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
##############################################################################  
### wkhtmltopdf  
##############################################################################  
### Ubuntu repositories' package depends on an X-Window server installed.  
### We use wkhtmltopdf.org binary download.  
### Also install wkhtmltopdf standalone .deb package dependencies.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
libxrender1 \  
fontconfig \  
fonts-dejavu \  
fonts-droid \  
xfonts-75dpi \  
xvfb \  
&& \  
wget -O wkhtmltox.deb \  
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.2.1/wkhtmltox-0.12.2.1_linux-
jessie-amd64.deb \  
&& \  
dpkg -i wkhtmltox.deb && \  
rm -v wkhtmltox.deb && \  
ln -vs /usr/local/bin/wkhtmltopdf /usr/bin/wkhtmltopdf \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
##############################################################################  
  
ADD files/root/ /root/  
ADD files/usr/local/bin/* /usr/local/bin/  
ADD files/etc/default/cloe_run /etc/default/  
  
RUN \  
mkdir -vp \  
/code \  
/cloe \  
/etc/cloe_run/first-run.d \  
/etc/cloe_run/pre-run.d \  
/etc/cloe_run/post-run.d \  
/etc/cloe_run/last-run.d \  
/root/.ssh \  
&& \  
chmod -v a+x \  
/usr/local/bin/cloe_run \  
/usr/local/bin/hchk-ping \  
/usr/local/bin/multiposter-loader \  
/usr/local/bin/shutdown-selenium \  
&& \  
ln -vs /usr/local/bin/multiposter-loader /etc/cloe_run/pre-run.d/ && \  
ln -vs /usr/local/bin/hchk-ping /etc/cloe_run/pre-run.d/  
  
WORKDIR /code  
  
##############################################################################  
### Java  
##############################################################################  
COPY /server-jre-8u74-linux-x64.tar.gz /opt/  
  
RUN \  
tar xzvf /opt/server-jre-8u74-linux-x64.tar.gz -C /opt/ && \  
rm -rf server-jre-8u74-linux-x64.tar.gz && \  
rm /usr/bin/java && \  
ln -vs /opt/jdk/bin/java /usr/bin/java  
##############################################################################  
  
VOLUME \  
/cloe  
  
ADD files/root/.ssh/id_rsa /root/.ssh/  
ADD files/root/.ssh/id_rsa.pub /root/.ssh/  
ADD files/letsencrypt.pem /opt/jdk/jre/lib/letsencrypt.pem  
ADD files/firmaprofesional.pem /opt/jdk/jre/lib/firmaprofesional.pem  
ADD files/comodo.pem /opt/jdk/jre/lib/comodo.pem  
  
RUN \  
chmod -v 600 /root/.ssh/id_rsa && \  
keytool \  
-import \  
-trustcacerts \  
-keystore /opt/jdk/jre/lib/security/cacerts \  
-storepass changeit \  
-noprompt \  
-importcert \  
-alias letsencrypt \  
-file /opt/jdk/jre/lib/letsencrypt.pem \  
&& \  
keytool \  
-import \  
-trustcacerts \  
-keystore /opt/jdk/jre/lib/security/cacerts \  
-storepass changeit \  
-noprompt \  
-importcert \  
-alias firmaprofesional \  
-file /opt/jdk/jre/lib/firmaprofesional.pem \  
&& \  
keytool \  
-import \  
-trustcacerts \  
-keystore /opt/jdk/jre/lib/security/cacerts \  
-storepass changeit \  
-noprompt \  
-importcert \  
-alias comodo \  
-file /opt/jdk/jre/lib/comodo.pem  
  
RUN \  
git init && \  
git remote add origin git@bitbucket.org:referup/multiposter-loader.git && \  
ssh -T -oStrictHostKeyChecking=no git@bitbucket.org && \  
git pull origin master  
  
ENTRYPOINT [ "cloe_run", "${CLOE_RUN_BIN}" ]  

