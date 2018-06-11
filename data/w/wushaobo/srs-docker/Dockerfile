FROM debian:jessie  
  
COPY files/cn.list /etc/apt/sources.list  
RUN apt-get update && \  
apt-get install -y vim wget unzip telnet sudo net-tools locales-all python-pip
ffmpeg  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN wget -q https://github.com/ossrs/srs/archive/v2.0-r2.zip -P /tmp/ && \  
cd /tmp && \  
unzip v2.0-r2.zip && \  
rm -f v2.0-r2.zip && \  
mkdir -p /opt/srs/ && \  
mv srs-2.0-r2/trunk/* /opt/srs/ && \  
rm -rf srs-2.0-r2  
  
# for nginx gzip module  
RUN apt-get install zlib1g-dev  
  
WORKDIR /opt/srs  
RUN ./configure --with-hls --with-nginx --with-transcode --with-ingest --with-
stat --with-http-callback --with-http-server --with-http-api --log-trace \  
\--without-hds --without-ssl --without-dvr --without-ffmpeg --without-stream-
caster --without-librtmp --without-research --without-utest --without-gperf
--without-gmc --without-gmp --without-gcp --without-gprof --without-arm-
ubuntu12 --without-mips-ubuntu12 \  
\--jobs=4 --x86-x64 --log-trace && \  
make  
  
EXPOSE 1935  
EXPOSE 8080  
EXPOSE 80  
COPY config_generator /tmp/srs/config_generator  
RUN cd /tmp/srs/config_generator && \  
./setup_venv.sh && \  
cd -  
  
COPY files/nginx.conf /opt/srs/objs/nginx/conf/nginx.conf  
COPY files/gen_conf_and_run.sh /tmp/srs/gen_conf_and_run.sh  

