FROM ubuntu:16.04  
COPY run /bin/run  
COPY bootstrap /bin/bootstrap  
  
RUN /bin/bootstrap binaries  
RUN /bin/bootstrap kernel_modules 4.4.0-62-generic  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends openssl ca-certificates kmod \  
iproute2 iptables\  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/var/log/openvswitch", "/var/lib/openvswitch",
"/var/run/openvswitch", "/etc/openvswitch"]  
ENTRYPOINT ["run"]  

