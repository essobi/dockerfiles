FROM debian  
  
MAINTAINER Vensder vensder@gmail.com  
  
RUN apt-get update && apt-get install -y \  
python-twisted \  
subversion \  
\--no-install-recommends && \  
useradd -d /home/kippo -s /bin/bash -m kippo && \  
cd /home && \  
svn checkout http://kippo.googlecode.com/svn/trunk/ ./kippo && \  
apt-get autoremove -y subversion && \  
cd /home/kippo && \  
mv kippo.cfg.dist kippo.cfg && \  
rm -rf /home/kippo/.svn && \  
chown -R kippo:kippo /home/kippo && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV HOME /home/kippo  
  
EXPOSE 2222  
USER kippo  
WORKDIR /home/kippo  
CMD ["twistd", "--nodaemon", "-y", "kippo.tac", "--pidfile=kippo.pid"]  

