FROM busybox  
RUN adduser -D -h /tmp -u 1025 smtp  
COPY mail-sink /mail-sink  
CMD /mail-sink -i="0.0.0.0" -p="2525"  
USER smtp  

