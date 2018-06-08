FROM plexinc/pms-docker:latest  
  
RUN echo 'cat $HEALTHCHECK_FILE' >> /healthcheck.sh  
EXPOSE 32400/tcp 3005/tcp 8324/tcp 32469/tcp 32410/udp 32412/udp 32413/udp
32414/udp  
VOLUME /config /transcode  
ENTRYPOINT ["/init"]  

