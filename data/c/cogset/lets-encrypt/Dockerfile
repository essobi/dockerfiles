# Lets-Encrypt  
# Cogset Open Source Group  
FROM cogset/cron:latest  
  
MAINTAINER Cogset <cogset@funcuter.org>  
  
ENV LETS_ENCRYPT_VERSION v0.14.2  
# Install  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends wget git ca-certificates python3
\  
&& wget -O letsencrypt.tar.gz
"https://github.com/certbot/certbot/archive/$LETS_ENCRYPT_VERSION.tar.gz" \  
&& mkdir -p /usr/local/letsencrypt \  
&& tar -xzf letsencrypt.tar.gz -C /usr/local/letsencrypt --strip-components=1
\  
&& rm letsencrypt.tar.gz \  
&& ln -s /usr/local/letsencrypt/letsencrypt-auto /usr/bin/letsencrypt-auto \  
&& letsencrypt-auto certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY letsencrypt-*.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/letsencrypt-*.sh  
  
ENTRYPOINT ["letsencrypt-entrypoint.sh"]  
  
CMD ["tail"]  

