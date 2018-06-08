FROM java:8-jdk  
  
ENV NIFI_HOME /opt/nifi  
ENV PATH $NIFI_HOME/bin:$PATH  
RUN mkdir -p "$NIFI_HOME"  
WORKDIR $NIFI_HOME  
  
# Make sure system is updated  
RUN apt-get update && rm -rf /var/lib/apt/lists/*  
  
# Grab version of Nifi from an Apache mirror  
ENV NIFI_VERSION 0.7.0  
ENV NIFI_TGZ_URL
http://www.gtlib.gatech.edu/pub/apache/nifi/$NIFI_VERSION/nifi-$NIFI_VERSION-
bin.tar.gz  
RUN wget -O nifi.tar.gz "$NIFI_TGZ_URL"  
  
# Extract to workdir  
RUN tar -xvf nifi.tar.gz --strip-components=1  
  
# TODO: Set Up Volumes for conf and other repositories  
# Expose 8080 for UI, expose others as need for HTTP or DB access  
EXPOSE 8080  
CMD ["nifi.sh", "run"]  

