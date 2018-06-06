FROM watawuwu/debian:wheezy  
  
RUN \  
curl http://packages.treasuredata.com/GPG-KEY-td-agent | apt-key add - && \  
echo "deb http://packages.treasuredata.com/2/debian/wheezy/ wheezy contrib" >
/etc/apt/sources.list.d/treasure-data.list && \  
apt-get update && \  
apt-get install -y --force-yes adduser td-agent wget ca-certificates --no-
install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /var/log/td-agent && \  
sed -i "s/USER=td-agent/USER=root/g" /etc/init.d/td-agent && \  
sed -i "s/GROUP=td-agent/GROUP=root/g" /etc/init.d/td-agent  
  
ENV GEM_HOME /opt/td-agent/embedded/lib/ruby/gems/2.1.0/  
ENV GEM_PATH /opt/td-agent/embedded/lib/ruby/gems/2.1.0/  
ENV PATH /opt/td-agent/embedded/bin/:$PATH  
  
EXPOSE 24224  
  
ADD launch.sh /usr/local/bin/launch.sh  
  
CMD ["/usr/local/bin/launch.sh"]  

