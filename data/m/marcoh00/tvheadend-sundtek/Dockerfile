FROM marcoh00/tvheadend:latest  
  
  
RUN curl -o /tmp/sundtek_netinst.sh
"http://www.sundtek.de/media/sundtek_netinst.sh" && \  
chmod +x /tmp/sundtek_netinst.sh && \  
/tmp/sundtek_netinst.sh -easyvdr && \  
rm /tmp/sundtek_netinst.sh  
  
# We need to run multiple processes, so let's add S6 to the image  
ENV S6_VERSION="1.19.1.1"  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzvf /tmp/s6-overlay-amd64.tar.gz -C / && rm -rf /tmp/*  
  
# Setup S6  
RUN mkdir -p /log/mediasrv && chown -R nobody:nogroup /log  
COPY rootfs /  
  
VOLUME /tvh-data /log  
ENTRYPOINT ["/init", "/entrypoint.sh"]  
CMD ["-u", "tvheadend", "-g", "tvheadend", "-c", "/tvh-data/conf"]  

