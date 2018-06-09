FROM postgres:alpine  
RUN apk add \--update \--no-cache gcc musl-dev make curl && \  
su - postgres && \  
cd /tmp && \  
curl -L https://github.com/arkhipov/temporal_tables/archive/master.tar.gz >
master.tar.gz && \  
tar xvf master.tar.gz && \  
cd temporal_tables-master && \  
make && \  
make install && \  
apk del curl gcc musl-dev make && \  
rm -rf /var/cache/apk/*  

