FROM debian:jessie  
  
RUN apt-get update && apt-get install -y munin-node munin-plugins-extra  
  
RUN rm /etc/munin/plugins/*  
  
RUN \  
sed -ri 's/^log_file.*/# \0/; \  
s/^pid_file.*/# \0/; \  
s/^background 1$/background 0/; \  
s/^setsid 1$/setsid 0/; \  
' /etc/munin/munin-node.conf && \  
/bin/echo -e "cidr_allow 192.168.0.0/16\ncidr_allow 172.16.0.0/12\ncidr_allow
10.0.0.0/8" >> /etc/munin/munin-node.conf  
  
ADD munin-add-plugin /usr/local/bin  
  
ADD df.conf /etc/munin/plugin-conf.d/df  
ADD df_inode.conf /etc/munin/plugin-conf.d/df_inode  
  
RUN munin-add-plugin cpu && \  
munin-add-plugin df && \  
munin-add-plugin df_inode && \  
munin-add-plugin diskstats && \  
munin-add-plugin iostat && \  
munin-add-plugin load && \  
munin-add-plugin memory && \  
munin-add-plugin uptime && \  
munin-add-plugin vmstat && \  
munin-add-plugin users && \  
munin-add-plugin entropy  
  
CMD munin-node  

