FROM mpeterson/base:0.1  
MAINTAINER mpeterson <docker@peterson.com.ar>  
  
# Make APT non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Change this ENV variable to skip the docker cache from this line on  
ENV LATEST_CACHE 2014-05-01T22:00-03:00  
# Upgrade the system to the latest version  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# We want the latest stable version of java  
RUN sudo apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y --force-yes oracle-java7-installer curl xmlstarlet  
  
# Install packages needed for this image  
RUN curl -Lks -o /root/stash.tar.gz
http://www.atlassian.com/software/stash/downloads/binary/atlassian-
stash-3.1.3.tar.gz  
RUN /usr/sbin/useradd --create-home --home-dir /opt/stash --shell /bin/bash
stash  
RUN tar zxf /root/stash.tar.gz --strip=1 -C /opt/stash  
RUN rm /root/stash.tar.gz  
  
# This after the package installation so we can use the docker cache  
RUN mkdir /build  
ADD . /build  
  
# Starting the installation of this particular image  
# Modify the location of data  
VOLUME ["/data"]  
ENV DATA_DIR /data  
  
RUN ln -s $DATA_DIR /opt/stash-home  
ENV STASH_HOME /opt/stash-home  
RUN chown -R stash:stash /opt/stash  
RUN chown -R stash:stash /opt/stash-home  
  
RUN mv /opt/stash/conf/server.xml /opt/stash/conf/server-backup.xml  
  
RUN cp -a /opt/stash /opt/.stash.orig  
  
ENV CONTEXT_PATH ROOT  
  
EXPOSE 7990 7999  
# End of particularities of this image  
# Give the possibility to override any file on the system  
RUN cp -R /build/overrides/. / || :  
  
# Add run script  
RUN cp -R /build/run_stash.sh /sbin/run_stash.sh  
RUN chown root:root /sbin/run_stash.sh  
  
# Clean everything up  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /build  
  
CMD ["/sbin/run_stash.sh"]  

