FROM ubuntu:14.04  
# So that we can run as unprivileged user inside the container.  
RUN apt-get update && apt-get install -y squid && rm -rf /var/lib/apt/lists/*  
ADD squid.conf /etc/squid3/squid.conf  
  
EXPOSE 3128  
# The following flags have to be specified when starting this container:  
# -network  
# Refer to -help for documentation on them.  
ENTRYPOINT ["/usr/sbin/squid3", "-NYCd", "1"]

