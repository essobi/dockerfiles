# Asterisk image Docker file  
# No configuration files are created, but the directories are exposed as
Volumes  
FROM debian:jessie  
MAINTAINER Yves Nicolas <yves.nicolas@dynamease.com>  
  
  
# Creates the user under which asterisk will run  
ENV ASTERISKUSER pbxrunner  
ENV ASTERISKVER 13.9.0  
RUN groupadd -r $ASTERISKUSER && useradd -r -g $ASTERISKUSER $ASTERISKUSER \  
&& mkdir /var/lib/asterisk && chown $ASTERISKUSER:$ASTERISKUSER
/var/lib/asterisk \  
&& usermod --home /var/lib/asterisk $ASTERISKUSER  
  
# grab gosu for easy step-down from root  
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \  
&& curl -o /usr/local/bin/gosu -SL
'https://github.com/tianon/gosu/releases/download/1.1/gosu' \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get purge -y --auto-remove curl  
  
# Asterisk compilation and installation  
# installation of packets needed for installation  
RUN apt-get update && apt-get install -y uuid-dev build-essential libxml2-dev
libncurses5-dev libsqlite3-dev libssl-dev libxslt-dev libjansson-dev
libmysqlclient-dev  
  
# Getting the sources  
WORKDIR /tmp  
RUN mkdir src && cd src \  
&& apt-get install -y wget \  
&& wget
http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-$ASTERISKVER.tar.gz
\  
&& tar -xvzf asterisk-$ASTERISKVER.tar.gz  
  
#installation asterisk  
WORKDIR /tmp/src/asterisk-$ASTERISKVER  
RUN ./configure  
RUN cd menuselect && make menuselect && cd .. & make menuselect-tree  
RUN menuselect/menuselect --disable BUILD_NATIVE menuselect.makeopts  
RUN menuselect/menuselect --enable app_mysql --enable cdr_mysql
menuselect.makeopts  
RUN make && make install && make config  
  
# Alternative : install the package  
# RUN apt-get update && apt-get install -y wget asterisk  
#installation PHP et PHP AGI  
#RUN apt-get update && apt-get install -y php5 php5-json \  
# && cd /tmp && wget
http://sourceforge.net/projects/phpagi/files/latest/download \  
# && tar xvzf download \  
# && mv phpagi-2.20/* /var/lib/asterisk/agi-bin/ \  
# && chmod ugo+x /var/lib/asterisk/agi-bin/*.php  
#necessary files and package for google tts  
# sox - google tts agi - mpg 123  
RUN apt-get install -y sox mpg123 libwww-perl \  
&& cd /tmp && wget https://github.com/downloads/zaf/asterisk-
googletts/asterisk-googletts-0.6.tar.gz \  
&& tar xvzf asterisk-googletts-0.6.tar.gz \  
&& cp asterisk-googletts-0.6/googletts.agi /var/lib/asterisk/agi-bin/  
  
#Change ownership of asterisk files  
RUN chown -R $ASTERISKUSER:$ASTERISKUSER /var/lib/asterisk \  
&& chown -R $ASTERISKUSER:$ASTERISKUSER /var/spool/asterisk \  
&& chown -R $ASTERISKUSER:$ASTERISKUSER /var/log/asterisk \  
&& chown -R $ASTERISKUSER:$ASTERISKUSER /var/run/asterisk \  
&& chown -R $ASTERISKUSER:$ASTERISKUSER /etc/asterisk  
  
# add fail2ban  
RUN apt-get update && apt-get install -y fail2ban  
RUN mkdir /var/run/fail2ban && chown -R $ASTERISKUSER:$ASTERISKUSER
/var/run/fail2ban  
RUN touch /var/log/fail2ban.log && chown -R $ASTERISKUSER:$ASTERISKUSER
/var/log/fail2ban.log  
  
# Copy fail2ban cnofig  
COPY initconfigfiles/fail2ban/* /etc/fail2ban/  
RUN chown -R $ASTERISKUSER:$ASTERISKUSER /etc/fail2ban  
  
# install supervisor  
RUN apt-get update && apt-get install -y supervisor  
  
RUN chown -R $ASTERISKUSER:$ASTERISKUSER /etc/supervisor  
# RUN chown -R $ASTERISKUSER:$ASTERISKUSER /var/run/supervisor  
RUN chown -R $ASTERISKUSER:$ASTERISKUSER /var/log/supervisor  
COPY initconfigfiles/supervisor/conf.d /etc/supervisor/conf.d  
RUN ls -lha /etc/supervisor/conf.d  
RUN chown -R $ASTERISKUSER:$ASTERISKUSER /etc/supervisor  
  
#Expose outside volumes  
VOLUME /var/log/asterisk  
VOLUME /etc/asterisk  
VOLUME /var/lib/asterisk  
  
#Copy minimum configuration files so that it can start  
COPY initconfigfiles/asterisk/* /etc/asterisk/  
  
#Make asterisk port open  
EXPOSE 5060  
EXPOSE 8088  
EXPOSE 10000-10095  
WORKDIR /var/lib/asterisk  
# USER $ASTERISKUSER  
# run supervisor  
CMD ["supervisord", "-n"]  

