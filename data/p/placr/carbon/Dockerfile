FROM python:2.7  
  
COPY  config /tmp/config  
  
# Create users. Note carbon user has same uid as the one in visity/graphiteweb  
RUN addgroup --gid 30100 carbon  
RUN useradd -u 30106 -g carbon -s /bin/false carbon  
  
RUN pip install twisted==11.1.0 whisper==0.9.15  
RUN pip install \--install-option="--prefix=/opt/graphite" carbon==0.9.15  
  
# Copy configs into place and create needed dirs  
COPY config/ /opt/graphite/conf/  
  
ENV PYTHONPATH /opt/graphite/lib/  
ENV WHISPER_AUTOFLUSH False  
ENV MAX_UPDATES_PER_SECOND 500  
  
# Entry point script also sets environment variables in config files.  
COPY docker-entrypoint.sh /  
  
# Graphiteweb requires access to this folder and should be mounted to host  
# for persistence.  
VOLUME /opt/graphite/storage/whisper/  
  
EXPOSE 2003 2004 7002  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/opt/graphite/bin/carbon-cache.py", "--debug", "start"]  

