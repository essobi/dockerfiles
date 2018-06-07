  
FROM marcelmaatkamp/docker-gnuradio-dump1090  
  
# To sign up for the first time and acquire a flightradar24 key:  
# $ docker run -ti marcelmaatkamp/flightradar24-feeder --signup  
# After that start the feeder with the key:  
# $ docker run -d \  
# --name flightradar_feeder \  
# --restart=always \  
# --privileged \  
# -p 8080:8080 \  
# -p 8754:8754 \  
# -p 30001:30001 \  
# -p 30002:30002 \  
# -p 30003:30003 \  
# -p 30334:30334 \  
# marcelmaatkamp/flightradar24-feeder \  
# --fr24key=<flightradar24 signup key>  
RUN apt-get update  
RUN apt-get install -y wget  
  
RUN wget https://ftp.gnu.org/gnu/gcc/gcc-4.9.3/gcc-4.9.3.tar.gz  
RUN tar -zxvf gcc-4.9.3.tar.gz  
RUN cd gcc-4.9.3/  
  
RUN apt-get install -y gcc  
RUN apt-get install -y zip  
  
RUN ./contrib/download_prerequisites --disable-multilib--enable-language=c,c++  
RUN ./configure --disable-multilib --enable-language=c,c++  
RUN make && make install  
  
RUN wget
http://ftp.vim.org/ftp/pub/ftp/os/Linux/distr/redsleeve/steam/glibc-2.15-60.el6.x86_64.rpm  
RUN wget http://ftp.vim.org/ftp/pub/ftp/os/Linux/distr/redsleeve/steam/glibc-
common-2.15-60.el6.x86_64.rpm  
RUN wget http://ftp.vim.org/ftp/pub/ftp/os/Linux/distr/redsleeve/steam/glibc-
devel-2.15-60.el6.x86_64.rpm  
RUN wget http://ftp.vim.org/ftp/pub/ftp/os/Linux/distr/redsleeve/steam/glibc-
headers-2.15-60.el6.x86_64.rpm  
  
RUN rpm -Uvh glibc-2.15-60.el6.x86_64.rpm glibc-common-2.15-60.el6.x86_64.rpm
glibc-devel-2.15-60.el6.x86_64.rpm glibc-headers-2.15-60.el6.x86_64.rpm  
RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib64  
  
RUN wget http://feed.flightradar24.com/linux/fr24feed_1.0.18-5_amd64.tgz  
RUN tar zxf fr24feed_1.0.18-5_amd64.tgz  
  
ADD fr24feed.ini /etc/fr24feed.ini  
  
WORKDIR fr24feed_amd64  
  
EXPOSE 8080  
EXPOSE 8754  
EXPOSE 30001  
EXPOSE 30002  
EXPOSE 30003  
EXPOSE 30334  
ENTRYPOINT ["./fr24feed"]  

