FROM cassandra  
RUN apt-get update && apt-get install -y dnsutils && rm -rf
/var/lib/apt/lists/*  
ADD ./files/docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh","cassandra","-f"]

