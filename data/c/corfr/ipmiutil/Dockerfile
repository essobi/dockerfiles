FROM debian:latest  
  
RUN apt-get update -y  
RUN apt-get install -y wget  
RUN apt-get install -y libssl1.0.0  
RUN ( \  
wget -q
http://ipmiutil.sourceforge.net/FILES/ipmiutil_2.9.6-1_debian_amd64.deb && \  
dpkg -i ipmiutil_2.9.6-1_debian_amd64.deb \  
)  
  

