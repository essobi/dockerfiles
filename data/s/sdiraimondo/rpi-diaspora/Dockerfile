FROM resin/rpi-raspbian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV POSTGRESQLTMPROOT temprootpass  
  
# Update and upgrade  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y software-properties-common python-software-properties
apt-transport-https  
RUN echo 'deb http://mirrordirector.raspbian.org/raspbian/ jessie main contrib
non-free rpi' >> /etc/apt/sources.list  
RUN echo 'deb [arch=armhf] https://apt.dockerproject.org/repo raspbian-jessie
main' >> /etc/apt/sources.list  
RUN echo 'deb https://packagecloud.io/Hypriot/rpi/debian/ jessie main' >>
/etc/apt/sources.list  
RUN echo 'deb https://packagecloud.io/Hypriot/Schatzkiste/debian/ jessie main'
>> /etc/apt/sources.list  
#RUN echo 'deb http://archive.raspberrypi.org/debian/ jessie main' >>
/etc/apt/sources.list  
RUN gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv F76221572C52609D &&
gpg --export \--armor F76221572C52609D | apt-key add -  
RUN gpg --keyserver pgpkeys.mit.edu --recv-key 37BBEE3F7AD95B3F && gpg -a
--export 37BBEE3F7AD95B3F| apt-key add -  
RUN apt-get update && apt-get -y upgrade  
  
# Install Apache and PostgreSQL  
RUN apt-get install -y apache2 libpq-dev postgresql-9.4 && apt-get clean  
  
RUN cp /etc/ssl/private/ssl-cert-snakeoil.key
/var/lib/postgresql/9.4/main/server.key && \  
chown postgres:postgres /var/lib/postgresql/9.4/main/server.key && \  
chmod 740 /var/lib/postgresql/9.4/main/server.key  
RUN mkdir -p /var/run/postgresql/9.4-main.pg_stat_tmp  
RUN chown -R postgres:postgres /var/run/postgresql/9.4-main.pg_stat_tmp  
  
# Install diaspora*  
RUN git clone git@github.com:diaspberry/poky.git  
RUN cd poky  
RUN git clone git@github.com:diaspberry/meta-raspberrypi.git  
RUN git clone git@github.com:diaspberry/meta-diaspberry.git  
RUN git checkout -b krogoth origin/krogoth  
RUN source oe-init-build-env build  
  
# Configure diaspora*  
ADD install.sh /home/diaspora/install.sh  
ADD install_diaspora.sh /home/diaspora/install_diaspora.sh  
ADD start.sh /home/diaspora/start.sh  
ONBUILD ADD database.yml /home/diaspora/diaspora/config/database.yml  
ONBUILD ADD diaspora.yml /home/diaspora/diaspora/config/diaspora.yml  
ONBUILD ADD diaspora.crt /home/diaspora/diaspora.crt  
ONBUILD ADD diaspora.key /home/diaspora/diaspora.key  
ONBUILD RUN /home/diaspora/install.sh  

