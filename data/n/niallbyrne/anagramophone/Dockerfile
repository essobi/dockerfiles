FROM ubuntu:14.04  
MAINTAINER Niall Byrne <reading.crows@gmail.com>  
  
# Update and tools  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y git python python-pip  
  
# Install Python Modules  
RUN \  
pip install flask-restful-swagger  
  
# Install applications  
RUN mkdir -p /webservice/gitroot && cd /webservice/gitroot && \  
git clone https://github.com/niall-byrne/anagramophone.git && \  
cd anagramophone && git checkout 1.2 && \  
cp webservice/anagramophone.service /etc/init.d/anagramophone && \  
update-rc.d anagramophone defaults && \  
/usr/bin/touch /webservice/gitroot/anagramophone/webservice/webservice.log  
RUN chmod +x /etc/init.d/anagramophone  
RUN useradd -r anagramophone -d /webservice  
RUN chown -R anagramophone:anagramophone /webservice  
  
CMD /bin/bash /etc/init.d/anagramophone start && \  
/usr/bin/tail -f /webservice/gitroot/anagramophone/webservice/webservice.log  

