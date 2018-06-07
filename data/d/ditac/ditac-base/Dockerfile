FROM java:8  
MAINTAINER Eliot Kimber "ekimber@contrext.com"  
ENV VERSION 2_5_7  
ENV HOME /home/ditac  
ENV PATH $HOME/bin:$PATH  
WORKDIR /home  
RUN wget -c http://www.xmlmind.com/ditac/_download/ditac-${VERSION}.zip &&
unzip ditac-${VERSION}.zip && \  
rm ditac-${VERSION}.zip  
# Use a consistent name for the directory so we don't have to worry about it  
RUN mv ditac-${VERSION} ditac  
# Set execution permissions on ant/bin directory  
RUN chmod a+rwx $HOME/bin/*  
# Put the bin directory in the path:  
WORKDIR $HOME  
# Prepare the /opt/ditac/ditac directory  
# so it can be used as a volume:  
RUN ln -s $DITA_HOME /opt/ditac/ditac  
#  
# Declare volumes intended to be mount points for  
# host directories:  
VOLUME /opt/ditac/data  
VOLUME /opt/ditac/out  
#  
# End of Dockerfile  
#

