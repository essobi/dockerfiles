FROM ubuntu:16.04  
RUN apt-get update && apt-get -y install nginx python3.5 python3-requests
psmisc curl vim && rm -rf /var/lib/apt/lists/*  
#COPY nginx.conf /etc/nginx/nginx.conf  
COPY update.py /root/update.py  
COPY setCloudflareDNS.sh /root/setCloudflareDNS.sh  
COPY rc.local /etc/rc.local  
  
RUN sed -idefault 's/# server_names_hash_bucket_size
64/server_names_hash_bucket_size 128/gi' /etc/nginx/nginx.conf && \  
sed -idefault 's/# worker_connections 768/worker_connections 5000/gi'
/etc/nginx/nginx.conf && \  
chmod +x /root/update.py && \  
chmod +x /etc/rc.local && \  
sed -i '11 a client_max_body_size 1000M;' /etc/nginx/nginx.conf  
  
WORKDIR /etc/nginx/conf.d/  
  
# add tcp lb stream config files to main nginx.conf  
COPY nginx.conf-patch /etc/nginx/nginx.conf-patch  
RUN cat /etc/nginx/nginx.conf-patch >> /etc/nginx/nginx.conf  
  
CMD ["/etc/rc.local"]  

