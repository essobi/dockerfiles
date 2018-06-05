FROM ubuntu  
  
ENV TWIT_SOURCE=""  
ENV TWIT_DESTINATION=""  
ENV TWIT_PARAMS=""  
RUN buildDeps="wget" \  
&& apt-get update \  
&& apt-get install -y $buildDeps \  
&& wget https://github.com/bander2/twit/releases/download/1.1.0/twit-linux-
amd64 \  
-O /usr/local/bin/twit --secure-protocol=TLSv1 \  
&& chmod a+x /usr/local/bin/twit \  
&& apt-get remove -y $buildDeps \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

