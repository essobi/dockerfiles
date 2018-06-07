FROM java:latest  
MAINTAINER Eliot Kimber "ekimber@contrext.com"  
ENV OT_VERSION 3.0.4  
LABEL ot-version ${OT_VERSION}  
ENV CATALOG_DIR /opt/dita-ot/catalogs  
# Make directories for later use  
RUN mkdir -p /opt/dita-ot/catalogs  
RUN chmod -R a+rwx /opt  
  
RUN useradd -u 5555 -ms /bin/bash dita-ot  
  
ENV HOME /home/dita-ot  
ENV DITA_HOME $HOME/DITA-OT  
# For OT 2.x the ant script is in the top-level bin/ dir  
ENV ANT_HOME $DITA_HOME  
ENV PATH $ANT_HOME/bin:$DITA_HOME:$PATH  
USER 5555  
WORKDIR $HOME  
RUN wget -c https://github.com/dita-ot/dita-
ot/releases/download/${OT_VERSION}/dita-ot-${OT_VERSION}.zip  
# For doing lots of builds to avoid fetching each time.  
RUN unzip dita-ot-${OT_VERSION}.zip && \  
rm dita-ot-${OT_VERSION}.zip  
# Use a consistent name for the OT so we don't have to worry about it  
RUN mv dita-ot-${OT_VERSION} DITA-OT  
# Set execution permissions on ant/bin directory  
RUN chmod a+rwx $DITA_HOME/bin/*  
# Put the bin directory in the path:  
ENV PATH $HOME/DITA-OT/bin:$PATH  
WORKDIR $DITA_HOME  
# Prepare the /opt/dita-ot/DITA-OT directory  
# so it can be used as a volume:  
RUN ln -s $DITA_HOME /opt/dita-ot/DITA-OT  
#  
# Declare volumes intended to be mount points for  
# host directories:  
VOLUME /opt/dita-ot/data  
VOLUME /opt/dita-ot/out  
#  
# NOTE For OT 2.x, the dita command manages the Java classpath.  
#  
# End of Dockerfile  
#  

