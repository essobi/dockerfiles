FROM kibana:5.1.1  
MAINTAINER developers@khipu.com  
RUN usermod --uid 2000 kibana && groupmod --gid 2000 kibana && \  
find /usr -uid 999 -exec chown kibana:kibana {} + && \  
find /var -uid 999 -exec chown kibana:kibana {} + && \  
su - kibana -c "/usr/share/kibana/bin/kibana-plugin install x-pack"  

