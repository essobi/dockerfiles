# Docker image for MySQL Tuner script  
#  
# Build: docker build -t exoplatform/mysqltuner .  
#  
# Run: docker run -ti --rm exoplatform/mysqltuner  
#  
FROM ubuntu:16.04  
ENV TERM=xterm  
  
# Installing dependencies  
ENV DEBIAN_FRONTEND noninteractive  
# --force-confold: do not modify the current configuration file, the new
version is installed with a .dpkg-dist suffix. With this option alone, even
configuration  
# files that you have not modified are left untouched. You need to combine it
with  
# --force-confdef to let dpkg overwrite configuration files that you have not
modified.  
ENV _APT_OPTIONS -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--
force-confold"  
RUN apt-get -qq update \  
&& apt-get -qq -y upgrade ${_APT_OPTIONS} \  
&& apt-get -qq -y install ${_APT_OPTIONS} \  
# locales \  
wget \  
openssl \  
perl \  
perl-doc \  
mysql-client \  
&& apt-get -qq -y autoremove \  
&& apt-get -qq -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Installing MySQL Tuner  
RUN set -eux \  
&& echo "Downloading MySQL Tuner script ..." \  
&& wget https://raw.githubusercontent.com/major/MySQLTuner-
perl/master/mysqltuner.pl -O /mysqltuner.pl \  
&& wget https://raw.githubusercontent.com/major/MySQLTuner-
perl/master/basic_passwords.txt -O /basic_passwords.txt \  
&& wget https://raw.githubusercontent.com/major/MySQLTuner-
perl/master/vulnerabilities.csv -O /vulnerabilities.csv  
  
ENTRYPOINT ["perl", "/mysqltuner.pl"]  
CMD ["--help"]  

