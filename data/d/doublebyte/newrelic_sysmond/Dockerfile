FROM ubuntu:trusty  
  
MAINTAINER doublebyte <joana.simoes@geocat.net>  
  
#Install new relic server to monitor the container  
RUN apt-get update -q && apt-get install -yq ca-certificates wget procps && \  
echo deb http://apt.newrelic.com/debian/ newrelic non-free >>
/etc/apt/sources.list.d/newrelic.list && \  
wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
apt-get update -q && \  
apt-get install -y -qq newrelic-sysmond && \  
apt-get clean  
  
#Workaround for docker 1.11  
RUN echo "cgroup_style=0" >> /etc/newrelic/nrsysmond.cfg  
  
#enable memory stats  
  
CMD nrsysmond-config --set license_key=${NRSYSMOND_license_key} && \  
nrsysmond -c /etc/newrelic/nrsysmond.cfg -l /dev/stdout -f  
  

