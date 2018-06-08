FROM openjdk:8-jre  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
socat netcat procps && \  
rm -rf /var/lib/apt/lists/*  
  
## Copy entrypoint script(s)  
COPY *.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*.sh  

