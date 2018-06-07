FROM mariadb:10.3  
LABEL maintainer "h-otter <h-otter@outlook.jp>"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
dnsutils \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4567  
EXPOSE 4568  
EXPOSE 4444  
COPY entrypoint.sh /  
CMD ["/entrypoint.sh"]  

