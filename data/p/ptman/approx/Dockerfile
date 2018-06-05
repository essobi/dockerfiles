# vim: set ft=dockerfile:  
FROM debian:stretch-slim  
# Author with no obligation to maintain  
MAINTAINER Paul Tötterman <paul.totterman@iki.fi>  
RUN echo 'APT::Install-Recommends "false";' >
/etc/apt/apt.conf.d/00InstallRecommends && \  
echo '9999 stream tcp nowait approx /usr/sbin/approx approx' > /etc/inetd.conf
&& \  
apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
approx \  
openbsd-inetd \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
# The config can be replaced without rebuilding with mounting a file using -v  
COPY approx.conf /etc/approx/approx.conf  
# In case you wish to persist the cache  
VOLUME /var/cache/approx  
EXPOSE 9999  
CMD ["inetd", "-i"]  

