FROM ubuntu:14.04  
MAINTAINER Li Meng Jun "lmjubuntu@gmail.com"  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y git make gcc g++ automake autoconf libbz2-dev libz-dev  
  
RUN git clone https://github.com/yinqiwen/ardb.git && \  
cd ardb && \  
make && \  
cp src/ardb-server /usr/bin && \  
cp ardb.conf /etc && \  
cd .. && \  
yes | rm -r ardb  
  
RUN sed -e 's@home.*@home /var/lib/ardb@' \  
-e 's/loglevel.*/loglevel info/' -i /etc/ardb.conf  
  
RUN echo 'trusted-ip *.*.*.*' >> /etc/ardb.conf  
  
WORKDIR /var/lib/ardb  
  
EXPOSE 16379  
ENTRYPOINT /usr/bin/ardb-server /etc/ardb.conf  

