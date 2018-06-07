FROM ubuntu:16.04  
WORKDIR /tmp  
  
RUN apt-get update  
RUN apt-get -y install wget  
RUN wget https://repo.percona.com/apt/percona-release_0.1-4.xenial_all.deb  
RUN dpkg -i percona-release_0.1-4.xenial_all.deb  
RUN apt-get update  
RUN apt-get -y install percona-xtrabackup-24  
  
RUN wget
https://github.com/rlmcpherson/s3gof3r/releases/download/v0.5.0/gof3r_0.5.0_linux_amd64.tar.gz  
RUN tar -xzf gof3r_0.5.0_linux_amd64.tar.gz  
RUN mv gof3r_0.5.0_linux_amd64/gof3r /usr/local/bin  
  
ENV PORT 3306  
CMD xtrabackup --backup --datadir /var/lib/mysql --target-dir=/output
--host=$HOST \--port=$PORT \--user=$USER \--password=$PASSWORD
\--encrypt=AES256 --encrypt-key=$ENCRYPT_KEY \--stream=xbstream --compress |
gof3r put -b $AWS_S3_BUCKET -k $AWS_S3_FILENAME \--endpoint
s3-$AWS_REGION.amazonaws.com --no-md5

