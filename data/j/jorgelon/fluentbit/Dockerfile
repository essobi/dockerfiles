FROM fluent/fluent-bit:0.12  
COPY fluent-bit.conf /fluent-bit/etc/fluent-bit.conf  
COPY parsers.conf /fluent-bit/etc/parsers.conf  
  
ENTRYPOINT ["/fluent-bit/bin/fluent-bit"]  
  
CMD ["-c","/fluent-bit/etc/fluent-bit.conf"]  
  

