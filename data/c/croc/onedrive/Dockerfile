FROM debian:latest  
  
RUN apt-get update && apt-get install -y libcurl4-openssl-dev libsqlite3-dev
curl git make binutils gcc cpp xz-utils gpg  
#RUN cd /opt && curl -fsS https://dlang.org/install.sh | bash -s dmd && bash
source ~/dlang/dmd-2.076.1/activate  
RUN cd /opt && curl -fsS https://dlang.org/install.sh | bash -s dmd && ln -s
/root/dlang/dmd-*/linux/bin64/dmd /usr/local/bin/  
RUN cd /opt && git clone https://github.com/skilion/onedrive.git && cd
onedrive && make && make install && mkdir /config && cp -f ./config /config  
  
COPY files/start.sh /opt/start.sh  
RUN chmod 755 /opt/*.sh  
  
ENTRYPOINT /opt/start.sh  

