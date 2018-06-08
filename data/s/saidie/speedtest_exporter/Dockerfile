FROM alpine:3.7  
RUN wget -O /usr/bin/speedtest_exporter
'https://bintray.com/artifact/download/nlamirault/oss/speedtest_exporter-0.2.0_linux_386'
&& \  
chmod 755 /usr/bin/speedtest_exporter  
  
CMD /usr/bin/speedtest_exporter  

