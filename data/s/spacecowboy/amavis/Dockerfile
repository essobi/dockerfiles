FROM debian:jessie  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -q update  
RUN apt-get -qy upgrade  
RUN apt-get -qy remove exim4  
  
# Necessary  
RUN apt-get -qy install sudo amavisd-new spamassassin clamav-daemon  
  
# To be able to scan inside compressed files  
RUN apt-get -qy install p7zip arj bzip2 cabextract cpio file gzip \  
nomarch pax unzip zip zoo  
  
# Optional for better spam detection  
RUN apt-get -qy install libnet-dns-perl libmail-spf-perl pyzor razor  
  
# Make some space  
RUN apt-get autoclean && rm -rf /var/lib/apt/lists/*  
  
# Add clamav user to the amavis group and vice versa in order for  
# Clamav to have access to scan files:  
RUN adduser clamav amavis  
RUN adduser amavis clamav  
  
# Pre-populate database so we can start services  
RUN sudo -u clamav freshclam  
  
# Make sure log file has correct permissions  
RUN touch /var/log/amavis.log  
RUN chown amavis:amavis /var/log/amavis.log  
  
# Prepare spam filter database location  
RUN mkdir -p /var/spamassassin/bayes_db  
VOLUME /var/spamassassin/bayes_db  
  
# Copy the config file to enable spam and antivirus checking  
COPY 15-content_filter_mode /etc/amavis/conf.d/15-content_filter_mode  
COPY 50-user /etc/amavis/conf.d/50-user  
COPY sa-local.cf /etc/spamassassin/local.cf  
  
COPY learn.sh /usr/local/bin/learn.sh  
COPY run.sh /usr/local/bin/run.sh  
  
CMD /usr/local/bin/run.sh  

