FROM debian:latest  
  
  
RUN apt-get update && apt-get -y upgrade && apt-get install -y rsync curl apt-
transport-https debconf-utils && rm -r /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y \  
make sudo debootstrap php5-cli php5-curl php5-json procps \  
gcc g++  
  
RUN curl -o - https://www.domjudge.org/repokey.asc | apt-key add -  
  
COPY debconf.selections /tmp/debconf.selections  
RUN cat /tmp/debconf.selections | debconf-set-selections  
  
RUN \  
echo "deb https://domjudge.org/debian unstable/" >
/etc/apt/sources.list.d/domjudge.list && \  
echo "deb-src https://domjudge.org/debian unstable/" >>
/etc/apt/sources.list.d/domjudge.list && \  
apt-get update && \  
apt-get install -y libcgroup-dev domjudge-common domjudge-judgehost  
  
#RUN /usr/sbin/dj_make_chroot  
RUN rm -r /var/lib/apt/lists/*  
  
COPY restapi.secret /etc/domjudge/restapi.secret  
COPY start.sh /tmp/start.sh  
  
ENTRYPOINT ["/tmp/start.sh"]  
  

