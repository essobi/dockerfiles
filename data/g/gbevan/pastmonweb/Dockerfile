# docker build -t gbevan/pastmonweb .  
#  
# to run: see README.md  
#  
  
FROM ubuntu:trusty  
MAINTAINER Graham Bevan "graham.bevan@ntlworld.com"  
  
ENV DEBIAN_FRONTEND=noninteractive \  
LANG=C \  
LC_ALL=C \  
TAG=0.17.6  
  
RUN \  
apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y wget aptitude htop vim git traceroute dnsutils \  
curl ssh sudo psmisc gcc make build-essential pkg-config \  
libglib2.0-dev libpcap-dev libdbi-dev libdbd-pgsql flex \  
sysstat postgresql bison packaging-dev tree nginx php5 \  
php5-pgsql php5-fpm libpcre3-dev sysstat tcpdump \  
fonts-dejavu fonts-liberation php5-gd cron  
  
# transfig texlive-latex-base for documentation  
# libphp-jpgraph is ancient - install manually from jpgraph.net  
  
RUN \  
mkdir /var/run/sshd && \  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \  
sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config && \  
useradd \--create-home -s /bin/bash pastmon && \  
mkdir -p /home/pastmon/.ssh && \  
chmod 700 /home/pastmon/.ssh && \  
chown -R pastmon: /home/pastmon/.ssh && \  
echo -n 'pastmon:pastmon' | chpasswd && \  
mkdir -p /etc/sudoers.d && \  
echo "pastmon ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/pastmon && \  
chmod 0440 /etc/sudoers.d/pastmon && \  
echo "set modeline" > /etc/vim/vimrc.local && \  
echo "export TERM=vt100\nexport LANG=C\nexport LC_ALL=C" >
/etc/profile.d/dockenv.sh && \  
echo "export TERM=vt100\nexport LANG=C\nexport LC_ALL=C" >> /root/.bashrc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
wget http://jpgraph.net/download/download.php?p=1 -O jpgraph-3.0.7.tar.gz && \  
mkdir -p /usr/share/jpgraph && \  
tar -C /usr/share/jpgraph -zxvf jpgraph-3.0.7.tar.gz \--wildcards src/*
\--exclude "src/Examples" \--strip-components=1 && \  
rm -f jpgraph-3.0.7.tar.gz && \  
sed -i "s?//
define('TTF_DIR','/usr/share/fonts/truetype/');?define('TTF_DIR','/usr/share/fonts/truetype/dejavu/');?"
/usr/share/jpgraph/jpg-config.inc.php  
  
RUN \  
su - pastmon -c "git clone -b $TAG git://git.code.sf.net/p/pastmon/pastmon
pastmon" && \  
su - pastmon -c "\  
cd pastmon/PasTmon && \  
./bootstrap --enable-server $* && make && sudo make install && make clean \  
" && \  
cp /usr/local/pastmon/etc/nginx/pastmon /etc/nginx/sites-available/ && \  
ln -s /etc/nginx/sites-available/pastmon /etc/nginx/sites-enabled/pastmon && \  
rm -f /etc/nginx/sites-enabled/default && \  
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/"
/etc/postgresql/9.3/main/postgresql.conf && \  
echo "host pastmon2 pastmon 0.0.0.0/0 md5" >>
/etc/postgresql/9.3/main/pg_hba.conf && \  
/etc/init.d/postgresql start && \  
/usr/local/pastmon/bin/postgresql_admin/create_database_summary && \  
sed -i 's?;include_path = ".:/usr/share/php"?include_path =
"/usr/share/jpgraph"?' /etc/php5/fpm/php.ini && \  
mv /usr/local/pastmon/etc/pastmon_summary_example.conf
/usr/local/pastmon/etc/pastmon_summary.conf && \  
echo "0 19 * * * /usr/local/pastmon/bin/pastmon_summarise_level_2.pl --age=32
--interval=3600 --delete 2>&1 | logger -t pastmon_summarise_level_2.pl" >
/var/spool/cron/crontabs/pastmon && \  
chmod 600 /var/spool/cron/crontabs/pastmon && \  
chown pastmon:crontab /var/spool/cron/crontabs/pastmon  
  
ADD start-pastmon-web.sh /usr/local/pastmon/bin/  
# see --volumes-from in pastmon-web@service unit file  
#VOLUME ["/var/lib/postgresql"]  
#VOLUME ["/var/run/postgresql"]  
  
ENTRYPOINT ["/bin/bash", "/usr/local/pastmon/bin/start-pastmon-web.sh"]  
  
# Not needed as container uses host's ip namespace  
#EXPOSE 8080 5432  

