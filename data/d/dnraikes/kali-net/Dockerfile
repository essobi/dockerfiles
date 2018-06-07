#############################################  
# File: kali-net/Dockerfile  
# Author: Donald Raikes <don.raikes@oracle.com>  
# Date: 12/13/2016  
#############################################  
FROM dnraikes/kali-msf  
MAINTAINER Donald Raikes  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y \  
openvas nsis rpm alien \  
tcpdump wireshark rpcbind  
RUN /usr/bin/openvas-setup  
COPY assets/openvas/* /usr/local/bin/  
RUN chmod 777 /usr/local/bin/*  
  
# Configure openvas to listen on all interfaces not just 127.0.0.1:  
ENV GSASERVICE=/lib/systemd/system/greenbone-security-assistant.service \  
MANAGERSERVICE=/lib/systemd/system/openvas-manager.service \  
SCANNERSERVICE=/lib/systemd/system/openvas-scanner.service  
RUN sed -e 's/127.0.0.1/0.0.0.0/g' ${GSADSERVICE} ${MANAGERSERVICE}
${SCANNERSERVICE} -i  
  
expose 9391/tcp  
VOLUME {"/public,/var/lib/postgresql,/root"}  
WORKDIR /public  
ENTRYPOINT service postgresql start && /bin/bash  

