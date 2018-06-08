FROM opensuse:tumbleweed  
RUN zypper refresh && \  
zypper --non-interactive install bind && \  
zypper clean -a  
CMD ["/usr/sbin/named", "-g", "-c", "/mnt/named.conf"]  

