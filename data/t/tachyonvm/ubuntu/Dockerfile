FROM ubuntu:16.04  
# Tell systemd that it is being run in a container  
ENV container docker  
  
# Shutdown signal for systemd  
STOPSIGNAL 37  
# Remove unneccessary modules to speed up boot time  
RUN find /etc/systemd/system \  
/lib/systemd/system \  
-path '*.wants/*' \  
-not -name '*journald*' \  
-not -name '*systemd-tmpfiles*' \  
-not -name '*systemd-user-sessions*' \  
-exec rm \\{} \;  
  
RUN apt-get update  
  
# Add required dependency for serverspec to see open ports  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
dbus \  
iproute2 \  
iptables \  
net-tools \  
netcat  
  
# Allow services installed by apt-get to start automatically  
RUN sed -i'' /usr/sbin/policy-rc.d -e 's/exit 101/exit 0/' \  
&& mv /usr/bin/hostnamectl /usr/bin/hostnamectl_original  
  
COPY hostnamectl_wrapper /usr/bin/hostnamectl  
  
# Symlinked to the systemd binary  
CMD ["/sbin/init"]  

