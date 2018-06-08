FROM alpine:latest  
  
MAINTAINER Nicolas Zagulajew (freeeflyer) <docker.com@xoop.org>  
  
ENV RS_HOME=/var/rs  
  
RUN echo "Downloading RadicalSpam"  
ADD http://download.radicalspam.org/releases/radicalspam-server-stable.tar.gz
/tmp/radicalspam-server-stable.tar.gz  
ADD http://download.radicalspam.org/releases/radicalspam-server-
stable.tar.gz.md5 /tmp/radicalspam-server-stable.tar.gz.md5  
RUN echo "Checking md5" && \  
cd /tmp && \  
md5sum -c radicalspam-server-stable.tar.gz.md5  
  
RUN echo "Installing RadicalSpam" && \  
cd /usr/share && \  
tar --numeric-owner -xzf /tmp/radicalspam-server-stable.tar.gz && \  
rm /tmp/radicalspam-server-stable.tar.gz && \  
ln -sf /usr/share/rs /var/rs  
  
ENV PATH=/var/rs/etc/scripts:$PATH  
  
  
VOLUME ["/data" ]  
  
WORKDIR $RS_HOME  
  
CMD ["/start"]  
  
EXPOSE 25  

