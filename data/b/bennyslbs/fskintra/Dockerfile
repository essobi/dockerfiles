#  
# Dockerfile for fskintra  
#  
FROM debian:stable  
MAINTAINER bennyslbs@slbs.dk  
  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-get update  
#RUN apt-get install -y apt-utils  
RUN apt-get install -y python2.7 python-beautifulsoup python-mechanize  
# Cleanup apt cache  
RUN apt-get clean  
# Python docker does "rm -rf /var/lib/apt/lists/*", but seems not to be a good
idea (at least not outside docker)  
# Copy fskintra  
ENV FSKINTRA_INSTALLDIR /var/opt/fskintra  
COPY . $FSKINTRA_INSTALLDIR/.  
RUN ln -s $FSKINTRA_INSTALLDIR/fskintra.py /usr/local/bin/fskintra  
# Set environment variable  
ENV PYTHONIOENCODING UTF-8  
VOLUME /root/.skoleintra  
  
# Copy help file, and default cmd is to cat it  
CMD cat $FSKINTRA_INSTALLDIR/README.docker.md  

