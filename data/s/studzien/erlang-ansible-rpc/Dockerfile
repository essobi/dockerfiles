FROM debian:jessie  
MAINTAINER Rafał Studnicki <rafal.studnicki@erlang-solutions.com>  
  
RUN apt-get update && \  
apt-get install -y git \  
wget && \  
wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && \  
dpkg -i erlang-solutions_1.0_all.deb && \  
apt-get update && \  
apt-get install -y esl-erlang=1:17.5.3 && \  
apt-get autoremove -y \--purge && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -rf erlang-solutions_1.0_all.deb && \  
git clone https://github.com/studzien/erlang-ansible-rpc.git  
  
ADD run.sh /  
  
ENTRYPOINT ["/run.sh"]  

