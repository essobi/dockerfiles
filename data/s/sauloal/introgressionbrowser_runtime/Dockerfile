#docker build --rm -t sauloal/introgressionbrowser_runtime .  
  
FROM ubuntu:14.04.3  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#RUN bash -c "echo -e 'deb mirror://mirrors.ubuntu.com/mirrors.txt trusty main
restricted universe multiverse\ndeb mirror://mirrors.ubuntu.com/mirrors.txt
trusty-updates main restricted universe multiverse\ndeb
mirror://mirrors.ubuntu.com/mirrors.txt trusty-backports main restricted
universe multiverse\ndeb mirror://mirrors.ubuntu.com/mirrors.txt trusty-
security main restricted universe multiverse' > /etc/apt/sources.list" && cat
/etc/apt/sources.list  
# california  
ENV AMAZON=us-west-1  
# oregon  
#ENV AMAZON=us-west-2  
# sao paulo  
#ENV AMAZON=sa-east-1  
# dublin  
#ENV AMAZON=eu-west-1  
# frankfurt  
#ENV AMAZON=eu-central-1  
# singapore  
#ENV AMAZON=ap-southeast-1  
# tokio  
#ENV AMAZON=ap-northeast-1  
  
RUN bash -c "echo -e '\  
deb http://'$AMAZON'.clouds.archive.ubuntu.com/ubuntu/ trusty main restricted
universe multiverse\n\  
deb http://'$AMAZON'.clouds.archive.ubuntu.com/ubuntu/ trusty-updates main
restricted universe multiverse\n\  
deb http://'$AMAZON'.clouds.archive.ubuntu.com/ubuntu/ trusty-security main
restricted universe multiverse\n' \  
> /etc/apt/sources.list" && \  
cat /etc/apt/sources.list && \  
printenv | sort && \  
rm /var/lib/apt/lists/* -rvf && \  
rm -f /var/cache/apt/* -rfv && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y -f libapache2-mod-wsgi apache2 nano build-essential \  
checkinstall openssl sqlite3 libsqlite3-dev git nano \  
libfreetype6 libfreetype6-dev zlib1g-dev libjpeg62 libjpeg62-dev \  
pkg-config libblas-dev liblapack-dev gfortran zlib1g-dev && \  
apt-get install -y -f python-setuptools python-dev python-numpy python-scipy \  
python-matplotlib python-pandas python-sympy python-pip python-imaging \  
python-numpy pylint && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
a2enmod wsgi && a2enmod proxy && a2enmod proxy_http && a2enmod rewrite && \  
mkdir -p /etc/apache2/mods-available/  
# apt-get clean all && \  
# mkdir -p /var/lib/apt/lists/partial && \  
# chmod 755 /var/lib/apt/lists/partial && \  

