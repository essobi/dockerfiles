# Open Monitoring Distribution  
## Version: 0.2  
FROM debian:jessie  
MAINTAINER Stefan Schüller "sschueller@techdroid.com"  
ARG SITENAME=default  
  
ENV SITENAME=$SITENAME  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# disable ipv6  
RUN echo 'net.ipv6.conf.default.disable_ipv6 = 1' >
/etc/sysctl.d/20-ipv6-disable.conf; \  
echo 'net.ipv6.conf.lo.disable_ipv6 = 1' >>
/etc/sysctl.d/20-ipv6-disable.conf; \  
echo 'net.ipv6.conf.all.disable_ipv6 = 1' >>
/etc/sysctl.d/20-ipv6-disable.conf; \  
cat /etc/sysctl.d/20-ipv6-disable.conf; sysctl -p  
  
# Make sure package repository is up to date  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# add key  
RUN gpg --keyserver keys.gnupg.net --recv-keys F8C1CA08A57B9ED7  
RUN gpg --armor --export F8C1CA08A57B9ED7 | apt-key add -  
  
# Add OMD source  
RUN echo 'deb http://labs.consol.de/repo/stable/debian jessie main' >>
/etc/apt/sources.list  
RUN apt-get update  
  
# install omd-labs edition  
RUN apt-get install -y libpython2.7 locales tzdata wget gdebi-core net-tools
postfix omd-labs-edition  
  
#Set timezone  
RUN echo "Europe/Zurich" > /etc/timezone; dpkg-reconfigure tzdata  
  
#Set locale  
RUN export LANGUAGE=en_US.UTF-8; export LANG=en_US.UTF-8; export
LC_ALL=en_US.UTF-8; locale-gen en_US.UTF-8; dpkg-reconfigure locales  
  
RUN mkdir -p /omd/sites/  
  
# Set up a default site  
RUN omd create $SITENAME  
  
# We don't want TMPFS as it requires higher privileges  
RUN omd config $SITENAME set TMPFS off  
  
# use grafana  
RUN omd config $SITENAME set PNP4NAGIOS off  
RUN omd config $SITENAME set GRAFANA on  
RUN omd config $SITENAME set INFLUXDB on  
RUN omd config $SITENAME set NAGFLUX on  
RUN omd config $SITENAME set PNP4NAGIOS gearman  
  
# set core to nagios  
RUN omd config $SITENAME set CORE nagios  
  
# deafult gui  
RUN omd config $SITENAME set DEFAULT_GUI welcome  
RUN omd config $SITENAME set THRUK_COOKIE_AUTH off  
  
# Accept connections on any IP address, since we get a random one  
RUN omd config $SITENAME set APACHE_TCP_ADDR 0.0.0.0  
  
# Add watchdog script  
ADD watchdog.sh /opt/omd/watchdog.sh  
RUN chmod +x /opt/omd/watchdog.sh  
  
# Set up runtime options  
EXPOSE 5000  
ENTRYPOINT ["/opt/omd/watchdog.sh"]  

