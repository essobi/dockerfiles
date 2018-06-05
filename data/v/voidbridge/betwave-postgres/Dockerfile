FROM voidbridge/postgres:9.4  
MAINTAINER Voidbridge <developers@voidbridge.com>  
  
LABEL io.k8s.description="PostgreSQL database for use in BetWave stack" \  
io.k8s.display-name="BetWave PostgreSQL"  
  
COPY files /  
  
ENV PARTMAN_DATABASES=betwave  
  
# Fix permissions  
USER root  
RUN chown -R 26:26 /etc/pgsql  
USER 26  
  
VOLUME /etc/secrets  

