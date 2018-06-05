FROM golang  
  
RUN \  
apt-get update # && apt-get -y upgrade && \  
apt-get -y install python-software-properties python-setuptools  
  
ADD
https://foundationdb.com/downloads/f-afxudaxbxuuo/I_accept_the_FoundationDB_Community_License_Agreement/key-
value-store/3.0.5/foundationdb-clients_3.0.5-1_amd64.deb /tmp/foundationdb-
clients.deb  
  
RUN dpkg -i /tmp/foundationdb-clients.deb  
  

