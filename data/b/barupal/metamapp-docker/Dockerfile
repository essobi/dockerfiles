FROM ubuntu:16.04  
ENV BRANCH 2.0.6  
# Install.  
RUN \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:marutter/rrutter && \  
apt-get update && \  
apt-get install -y wget make devscripts apache2-dev apache2 libapreq2-dev
r-base r-base-dev libapparmor-dev libcurl4-openssl-dev libprotobuf-dev
protobuf-compiler xvfb xauth xfonts-base curl libssl-dev libxml2-dev libicu-
dev pkg-config libssh2-1-dev locales apt-utils && \  
useradd -ms /bin/bash builder  
  
# Different from debian  
RUN apt-get install -y language-pack-en-base  
  
USER builder  
  
RUN \  
cd ~ && \  
wget https://github.com/opencpu/opencpu-server/archive/v${BRANCH}.tar.gz && \  
tar xzf v${BRANCH}.tar.gz && \  
cd opencpu-server-${BRANCH} && \  
dpkg-buildpackage -us -uc  
  
USER root  
  
RUN \  
apt-get install -y libapache2-mod-r-base && \  
dpkg -i /home/builder/opencpu-lib_*.deb && \  
dpkg -i /home/builder/opencpu-server_*.deb  
  
RUN \  
apt-get install -y gdebi-core git sudo && \  
wget --quiet https://download2.rstudio.org/rstudio-server-1.1.383-amd64.deb &&
\  
gdebi --non-interactive rstudio-server-1.1.383-amd64.deb && \  
rm -f rstudio-server-1.1.383-amd64.deb  
  
# Prints apache logs to stdout  
RUN \  
ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \  
ln -sf /proc/self/fd/1 /var/log/apache2/error.log && \  
ln -sf /proc/self/fd/1 /var/log/opencpu/apache_access.log && \  
ln -sf /proc/self/fd/1 /var/log/opencpu/apache_error.log  
  
# Set opencpu password so that we can login  
RUN \  
echo "opencpu:opencpu" | chpasswd  
  
RUN apt-get install -y libcairo2-dev  
  
COPY R.install /tmp  
RUN Rscript /tmp/R.install && \  
rm /tmp/R.install  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y couchdb && \  
sed -i -r 's/;bind_address = 127.0.0.1/bind_address = 0.0.0.0/'
/etc/couchdb/local.ini && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
COPY MetaMapp2017_2.0.1.tar.gz /home/opencpu/  
  
COPY R_1.install /tmp  
RUN Rscript /tmp/R_1.install && \  
rm /tmp/R_1.install  
  
RUN mkdir /var/www/metamapp  
COPY metamapp.conf /etc/apache2/sites-available  
COPY .htaccess /var/www/metamapp  
RUN ln -s /etc/apache2/sites-available/metamapp.conf /etc/apache2/sites-
enabled  
  
RUN mkdir -p /etc/opencpu/  
COPY server.conf /etc/opencpu  
  
# Apache ports  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8004  
# CMD /usr/local/bin/run  
# CMD couchdb -b  
# Start non-daemonized webserver  
CMD sudo /usr/lib/rstudio-server/bin/rserver && apachectl -DFOREGROUND

