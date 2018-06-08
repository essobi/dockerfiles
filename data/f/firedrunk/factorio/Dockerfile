FROM fedora  
  
MAINTAINER Thijs Cramer <thijs.cramer@gmail.com>  
  
RUN dnf install -y wget findutils xz  
RUN dnf clean all  
RUN useradd -m -d /opt/factorio -s /bin/bash factorio  
RUN chown -R factorio:factorio /opt/factorio  
  
USER factorio  
  
ENV HOME /opt/factorio  
ENV SAVEFILE /opt/factorio/saves/factorio_save.zip  
#ENV VERSION experimental  
WORKDIR /opt/factorio  
  
RUN wget -q -O - https://www.factorio.com/download-headless/experimental | \  
grep -o -m1 "/get-download/.*/headless/linux64" | \  
awk '{print "--no-check-certificate https://www.factorio.com"$1" -O
/tmp/factorio.tar.xz"}' | \  
xargs wget \  
&& tar xf /tmp/factorio.tar.xz -C /opt \  
&& rm -f /tmp/factorio.tar.xz  
  
ADD run.sh /opt/factorio/  
  
VOLUME ["/opt/factorio","/opt/factorio/saves"]  
  
EXPOSE 34197/udp  
CMD ["./run.sh", "--"]  

