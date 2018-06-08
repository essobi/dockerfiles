FROM java:jre  
  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qq --no-install-recommends curl ca-certificates \  
&& mkdir /opt/jmxtrans /opt/jmxtrans/conf /opt/jmxtrans/log \  
&& curl -sSL -o /opt/jmxtrans/jmxtrans-all.jar
https://repo.stackdriver.com/jmxtrans/jmxtrans-all.jar \  
&& apt-get remove -qq --auto-remove curl \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["jmxtrans"]  

