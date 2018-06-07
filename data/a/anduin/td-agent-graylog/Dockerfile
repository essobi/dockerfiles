FROM anduin/consul-template  
  
MAINTAINER ductamnguyen@anduintransact.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install td-agent  
RUN apt-get update && apt-get install -y wget curl make g++ && \  
curl https://packages.treasuredata.com/GPG-KEY-td-agent | apt-key add - && \  
echo "deb http://packages.treasuredata.com/2/ubuntu/trusty/ trusty contrib" >
/etc/apt/sources.list.d/treasure-data.list && \  
apt-get update && \  
apt-get install -y --force-yes td-agent && \  
/usr/sbin/td-agent-gem install gelf && \  
td-agent-gem install --no-document fluent-plugin-kubernetes_metadata_filter  
  
RUN sed -i -e "s/USER=td-agent/USER=root/" -e "s/GROUP=td-agent/GROUP=root/"
/etc/init.d/td-agent  
  
# Clean up APT when done.  
RUN rm -rf /opt/td-agent/embedded/share/doc \  
/opt/td-agent/embedded/share/gtk-doc \  
/opt/td-agent/embedded/lib/postgresql \  
/opt/td-agent/embedded/bin/postgres \  
/opt/td-agent/embedded/share/postgresql  
  
RUN apt-get remove -y make g++ && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD start-td-agent.sh /  
ADD td-agent /etc/default/td-agent  
ADD out_gelf.rb /etc/td-agent/plugin/out_gelf.rb  
CMD /start-td-agent.sh  

