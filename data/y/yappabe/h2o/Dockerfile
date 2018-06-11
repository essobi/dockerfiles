FROM debian:jessie  
  
MAINTAINER Joeri Verdeyen <joeriv@yappa.be>  
  
ENV DOCUMENT_ROOT /var/www/app/web  
ENV PHP_FPM_SOCKET_HOST php  
ENV PHP_FPM_SOCKET_PORT 9000  
ENV INDEX_FILE app_dev.php  
  
RUN \  
apt-get update && \  
apt-get install -y \  
libuv-dev \  
libyaml-dev \  
libssl-dev \  
cmake \  
git \  
build-essential  
  
WORKDIR /tmp  
RUN git clone https://github.com/h2o/h2o.git  
WORKDIR /tmp/h2o  
  
RUN git submodule update --init --recursive  
RUN cmake . && \  
make h2o && \  
mv /tmp/h2o/h2o /usr/sbin/h2o && \  
mv /tmp/h2o/examples /etc/h2o && \  
rm -rf /tmp/h2o  
  
COPY h2o.conf /etc/h2o/h2o.conf  
COPY run.sh run.sh  
RUN chmod +x run.sh  
  
EXPOSE 80  
EXPOSE 443  
CMD ["./run.sh"]

