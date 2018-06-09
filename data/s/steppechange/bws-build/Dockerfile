FROM ubuntu:trusty  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y install \  
syslog-ng-core \  
wget \  
git \  
psmisc \  
build-essential \  
python-pip  
  
RUN pip install --upgrade pip && \  
pip install awscli  
  
RUN echo "SYSLOGNG_OPTS=\"--no-caps\"" >> /etc/default/syslog-ng  
  
RUN cd /tmp; wget https://packages.erlang-solutions.com/erlang-
solutions_1.0_all.deb && \  
dpkg -i erlang-solutions_1.0_all.deb  
  
RUN apt-get update && apt-get -y install \  
`apt-cache depends erlang=1:18.0 | awk '/Depends: erlang/{print$2"=1:18.0"}' |
awk -F= '$1!="erlang-base" {print}'`  
  
RUN apt-get -y install \  
erlang=1:18.0 \  
dh-autoreconf  
  
ENV GPROC_DIST=true  
ENV EXOMETER_PACKAGES="(basic)"  
ADD syslog-ng.conf /etc/syslog-ng/syslog-ng.conf  
ADD onstart.sh /root/onstart.sh  
  
CMD ["/root/onstart.sh"]  

