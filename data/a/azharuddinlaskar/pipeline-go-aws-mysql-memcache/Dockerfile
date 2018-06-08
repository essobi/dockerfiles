# Base the docker container off of matchmove/bitbucket-pipeline-go-aws-
mysql:latest  
FROM matchmove/bitbucket-pipeline-go-aws-mysql:latest  
  
RUN apt-get update -q  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
apt-utils  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install memcached  
  
RUN curl -O https://nodejs.org/dist/v6.10.1/node-v6.10.1.tar.gz  
  
RUN \  
tar -xvf node-v6.10.1.tar.gz &&\  
rm node-v6.10.1.tar.gz &&\  
cd node-v6.10.1 &&\  
./configure &&\  
make &&\  
make install  

