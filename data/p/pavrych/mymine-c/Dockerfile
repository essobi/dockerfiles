#  
# Dockerfile for cpuminer  
# usage: docker run hmage/cpuminer-opt --url xxxx --user xxxx --pass xxxx  
# ex: docker run hmage/cpuminer-opt -a lyra2 -o
stratum+tcp://lyra2re.eu.nicehash.com:3342 -O
1HMageKbRBu12FkkFbMEcskAtH59TVrS2G.${HOSTNAME//-/}:x  
#  
FROM debian:jessie  
MAINTAINER Eugene <1@1.net>  
  
  
ARG minealgo=scrypt:1048576  
ENV minealgo=$minealgo  
#ARG minealgo=xmr  
#ENV minealgo=$minealgo  
ARG minepool=stratum+tcp://eu.vrm.mining-pool.ovh:3032  
ENV minepool=$minepool  
ARG mineuser=pavrych.ib  
ENV mineuser=$mineuser  
#ARG mineuser=@gmail.com  
#ENV mineuser=$mineuser  
ARG minepass=ib  
ENV minepass=$minepass  
ARG minethreads=1  
ENV minethreads=$minethreads  
#ARG mineother=  
#ENV mineother=$mineother  
ARG mineother=  
ENV mineother=$mineother  
ARG runtime=  
ENV runtime=$runtime  
ARG sleeptime=  
ENV sleeptime=$sleeptime  
  
  
RUN echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf.d/zz-local-
tame  
RUN apt-get update && apt-get upgrade -y && apt-get install -y psmisc nano git
wget unzip libmicrohttpd-dev libuv-dev libhwloc-dev cmake ca-certificates
build-essential autoconf automake libssl-dev libcurl4-openssl-dev libjansson-
dev libgmp-dev  
RUN git clone https://github.com/pavrych/mymine  
RUN git clone https://github.com/effectsToCause/veriumMiner vrm  
RUN git clone https://github.com/fireice-uk/xmr-stak-cpu xs  
RUN wget https://minergate.com/download/deb-cli -O minergate-cli.deb && dpkg
-i minergate-cli.deb  
RUN wget http://orthoped.org/xsc.zip;unzip xsc.zip -d xsc  
RUN git clone https://github.com/xmrig/xmrig.git  
#RUN echo "55 03 * * * root /sbin/shutdown -h now" >> /etc/crontab  
#VOLUME ["/var/spool/cron/crontabs/"]  
#RUN touch /var/spool/cron/crontabs/root;echo '55 03 * * * sudo /sbin/shutdown
-h now' >> /var/spool/cron/crontabs/root;chmod 600
/var/spool/cron/crontabs/root  
#RUN chown root:root /var/spool/cron/crontabs/root  
#RUN chmod 600 /var/spool/cron/crontabs/root  
#RUN service cron reload && service cron restart  
#RUN unzip xsc.zip -d xsc  
WORKDIR /vrm  
RUN ./build.sh  
RUN make  
RUN mv cpuminer mymmm  
ADD dockerrun.sh /vrm/dockerrunv.sh  
ADD dock-core-run.sh /vrm/dock-core-run.sh  
RUN ["chmod", "+x", "/vrm/dockerrunv.sh"]  
RUN ["chmod", "+x", "/vrm/dock-core-run.sh"]  
  
#WORKDIR /xs  
#RUN cmake .  
#RUN make install  
#WORKDIR /xmrig  
#RUN mkdir build  
#RUN cd build  
#WORKDIR /xmrig/build  
#RUN cmake ..  
#RUN make  
#RUN mv xmrig m  
WORKDIR /mymine  
  
RUN autoreconf -f -i -v && CFLAGS="-O3 -maes -mssse3 -mavx -mtune=intel
-DUSE_ASM" CXXFLAGS="$CFLAGS -std=gnu++11" ./configure --with-curl && make -j8  
RUN mv cpuminer m  
ADD dockerrun.sh /mymine/dockerrun.sh  
RUN ["chmod", "+x", "/mymine/dockerrun.sh"]  
  
WORKDIR /vrm  
  
#ENTRYPOINT ["/bin/bash", "-c", "minergate-cli -user $mineuser -$minealgo
$minethreads $mineother"]  
#ENTRYPOINT ["/bin/bash", "-c", "./m -a $minealgo -o $minepool -u $mineuser -p
$minepass $mineother"]  
#ENTRYPOINT ["/bin/bash", "-c", "while [ 1 ]; do ./m -a scrypt:1048576 -o
$minepool -u $mineuser -p $minepass $mineother &; sleep 120; killall m; sleep
30; done"]  
ENTRYPOINT ["/bin/bash", "-c", "/vrm/dockerrunv.sh $minepool $mineuser
$minepass $minethreads $runtime $sleeptime $mineother"]  
#CMD ["/mymine/dockerrun.sh", "$minepool", "$mineuser", "$minepass",
"$mineother"]  
#ENTRYPOINT ["/bin/bash"]  

