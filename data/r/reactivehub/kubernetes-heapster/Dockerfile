FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HEAPSTER_VERSION v0.16.1  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qq --no-install-recommends curl ca-certificates \  
&& curl -sSL -o /heapster
https://github.com/GoogleCloudPlatform/heapster/releases/download/$HEAPSTER_VERSION/heapster
\  
&& chmod +x /heapster \  
&& apt-get remove -qq --auto-remove curl \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["heapster"]  

