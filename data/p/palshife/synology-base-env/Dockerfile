FROM debian  
WORKDIR /syno-base  
RUN apt-get update \  
&& apt-get install -y wget tar xz-utils  
RUN wget -qO -
https://sourceforge.net/projects/dsgpl/files/toolkit/DSM6.1/base_env-6.1.txz |
tar -xJ  
  
FROM scratch  
COPY \--from=0 /syno-base /  
RUN /usr/bin/update-ca-trust  

