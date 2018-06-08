  
FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y git \  
&& rm -r /var/lib/apt/lists/*  
  
# wget https://github.com/letsencrypt/letsencrypt/archive/v0.4.2.tar.gz  
ADD v0.4.2.tar.gz /usr/local/  
  
# Does a lot of package installations that we don't want at runtime.  
# Prints a "No installers" error but that's normal.  
RUN cd /usr/local/letsencrypt-0.4.2 \  
&& ./letsencrypt-auto; exit 0  
  
RUN ln -s /root/.local/share/letsencrypt/bin/letsencrypt
/usr/local/bin/letsencrypt  
  
COPY cert-sync /usr/local/bin/  
  
# Commented out because we don't want defaults  
#ENV cert_domains  
#ENV cert_email  
#ENV LETSENCRYPT_ENDPOINT  
ENTRYPOINT cert-sync  

