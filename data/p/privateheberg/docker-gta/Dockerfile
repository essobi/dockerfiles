# ==================  
# GTARP Dockerfile  
# PrivateHeberg©  
# ==================  
FROM debian:8  
MAINTAINER privateHeberg  
  
# ==== Variables ==== #  
ENV PORT=30120  
# =================== #  
# ==== Paquets ==== #  
RUN apt-get update &&\  
apt-get upgrade -y &&\  
apt-get install -y wget &&\  
apt-get install -y unzip &&\  
apt-get install -y make &&\  
apt-get install -y screen &&\  
apt install -y bzip2 &&\  
apt install -y g++ &&\  
apt install -y cmake &&\  
apt install -y gcc &&\  
apt-get install -y automake &&\  
apt-get install -y libtool &&\  
apt-get install -y gettext &&\  
apt-get install -y cmake &&\  
apt-get install -y python2.7 &&\  
apt-get install -y build-essential  
  
# ================= #  
# ==== Gta user ==== #  
RUN adduser \  
\--disabled-login \  
\--shell /bin/bash \  
\--gecos "" \  
gta  
RUN usermod -a -G sudo gta  
# ==================== #  
# ==== Scripts ==== #  
RUN touch /root/.bash_profile  
RUN mkdir /data  
COPY start.sh /home/gta/start.sh  
RUN chmod 777 /home/gta/start.sh  
RUN chown gta -R /data && chmod 777 -R /data  
# ================= #  
# ==== Volumes ==== #  
VOLUME /data  
WORKDIR /data  
# ================= #  
# ==== Volumes ==== #  
EXPOSE $PORT  
# ================= #  
  
ENTRYPOINT ["/home/gta/start.sh"]  

