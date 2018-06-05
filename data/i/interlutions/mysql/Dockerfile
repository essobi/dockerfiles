FROM mysql:5.7  
# Tools to change the uid on run  
RUN apt-get update && \  
apt-get install -y --no-install-recommends sudo && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
COPY entrypoint-chuid /usr/local/bin  
ENTRYPOINT ["entrypoint-chuid"]  
CMD ["mysqld"]  

