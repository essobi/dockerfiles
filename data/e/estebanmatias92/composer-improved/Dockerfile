FROM estebanmatias92/composer-hhvm  
  
MAINTAINER "Matias Esteban" <estebanmatias92@gmail.com>  
  
# Install runtime dependencies  
RUN deps=' \  
wget \  
unzip \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends $deps && rm
-rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["composer"]  

