# Nagios server with web config UI  
FROM mhvelplund/nagios:1.0.2  
MAINTAINER Mads Hvelplund "mhv@tmnet.dk"  
## Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq  
RUN apt-get install -y php5-mysqlnd  
  
# Download NagiosQL  
ADD
http://downloads.sourceforge.net/project/nagiosql/nagiosql/NagiosQL%203.2.0/nagiosql_320.tar.gz
/download/nagiosql_320.tar.gz  
WORKDIR /download  
RUN tar xvzf nagiosql_320.tar.gz  
WORKDIR /  
  
# Install  
RUN mv /download/nagiosql32 /usr/local/nagiosql  
ADD nagiosql.conf /etc/apache2/conf-available/nagiosql.conf  
RUN a2enconf nagiosql  
  
# Configure  
RUN ln -s /usr/local/nagios/etc /etc/nagios  
ADD settings.php /usr/local/nagiosql/config/settings.php  
ADD etc /etc/nagiosql  
ADD nagioscfg.append /nagioscfg.append  
ADD confignagiosql.sh /confignagiosql.sh  
RUN /confignagiosql.sh  
RUN /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg  
  
# Patch PHP's config  
RUN sed -e 's/;date.timezone =/date.timezone = UTC/' /etc/php5/apache2/php.ini
> /tmp.ini  
RUN mv /tmp.ini /etc/php5/apache2/php.ini  
  
# Cleanup  
RUN rm -rf /download  
RUN rm -f /nagioscfg.append  
RUN rm -f /confignagiosql.sh  

