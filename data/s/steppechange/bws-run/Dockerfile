FROM phusion/baseimage:0.9.14  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y install \  
wget \  
ntp \  
git \  
psmisc \  
build-essential \  
python-pip  
  
RUN cd /usr/bin; wget
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O jq;
chmod +x jq  
  
RUN pip install --upgrade pip && \  
pip install awscli  
  
RUN cd /tmp; wget https://packages.erlang-solutions.com/erlang-
solutions_1.0_all.deb && \  
dpkg -i erlang-solutions_1.0_all.deb  
  
RUN apt-get update && apt-get -y install \  
`apt-cache depends erlang=1:18.0 | awk '/Depends: erlang/{print$2"=1:18.0"}' |
awk -F= '$1!="erlang-base" {print}'`  
  
RUN apt-get install -y \  
erlang=1:18.0  
  
ADD ntp.conf /etc/ntp.conf  
  
RUN mkdir /etc/service/button  
ADD onstart.sh /etc/service/button/run  
ADD ntpd.sh /etc/service/ntpd/run  
  
CMD ["/sbin/my_init"]  

