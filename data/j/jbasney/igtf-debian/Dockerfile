# docker build -t jbasney/igtf-debian .  
# docker run --name igtf-debian -it jbasney/igtf-debian /bin/bash  
FROM debian  
MAINTAINER Jim Basney <jbasney@illinois.edu>  
ENV container docker  
RUN apt-get update && apt-get install -y apt-transport-https apt-utils gnupg  
COPY igtf.list /etc/apt/sources.list.d  
COPY GPG-KEY-EUGridPMA-RPM-3 /root  
RUN apt-key add /root/GPG-KEY-EUGridPMA-RPM-3  
RUN apt-get update && apt-get install -y \  
ca-policy-igtf-classic \  
ca-policy-igtf-mics \  
ca-policy-igtf-slcs \  
ca-policy-igtf-iota  

