FROM seldszar/icecast:2.4.3  
# Copy the configuration file on build  
ONBUILD COPY icecast.xml /etc/icecast2/  
ONBUILD RUN chown -R icecast2 /etc/icecast2/icecast.xml  

