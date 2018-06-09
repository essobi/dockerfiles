FROM debian:jessie  
  
ENV STELLAR_CORE_VERSION 9.2.0-586-a60dead7  
ENV HORIZON_VERSION 0.12.3  
EXPOSE 8000  
WORKDIR /opt/horizon  
  
ADD install-linux-amd64 /tmp/horizon-install  
RUN bash /tmp/horizon-install  
RUN apt install -y curl postgresql-client  
  
ENV POSTGRES_UNIX_SOCKET "/postgresql-unix-sockets"  
ENV POSTGRES_USERNAME "postgres"  
ENV POSTGRES_DBNAME "horizon"  
ENV POSTGRES_CORE_UNIX_SOCKET "/postgresql-unix-sockets"  
ENV POSTGRES_CORE_USERNAME "postgres"  
ENV POSTGRES_CORE_DBNAME "stellar"  
ENV NETWORK_PASSPHRASE "Public Brave Stellar Network ; April 2018"  
ADD entrypoint /opt/horizon/entrypoint  
  
ENTRYPOINT [ "/opt/horizon/entrypoint" ]  

