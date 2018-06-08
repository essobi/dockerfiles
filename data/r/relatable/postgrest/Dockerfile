FROM nginx:latest  
  
# bizarre error when installing postgresql-client  
# requires making man folders  
RUN mkdir -p /usr/share/man/man7 && \  
mkdir -p /usr/share/man/man1 && \  
apt-get update && apt-get install -y curl \  
postgresql-client \  
xz-utils && \  
mkdir /postgrest && \  
cd /postgrest && \  
curl -L -O
https://github.com/begriffs/postgrest/releases/download/v0.4.1.0/postgrest-0.4.1.0-ubuntu.tar.xz
&& \  
tar xfJ postgrest-0.4.1.0-ubuntu.tar.xz  
  
COPY postgrest.conf wait-for-postgres.sh /postgrest/  
  
WORKDIR /postgrest  
  
EXPOSE 3000  

