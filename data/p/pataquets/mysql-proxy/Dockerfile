FROM pataquets/ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
mysql-proxy \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
EXPOSE 3306  
EXPOSE 4041  
  
ENTRYPOINT [ "mysql-proxy", "--proxy-address=0.0.0.0:3306" ]  
CMD [ "--help-all" ]  
  
# For another derived image:  
#CMD [ "--keepalive", "--log-level=level=message", "--proxy-backend-
addresses=mysql:3306" ]  
  
# \--help-all  
# \--proxy-backend-addresses=mysql:3306  
  
# \--proxy-skip-profiling  
# \--proxy-backend-addresses=host:port  
# \--proxy-read-only-backend-addresses=host:port  
# \--keepalive  
  
# \--log-level=level=crititcal  
# The log level to use when outputting error messages. Messages with that
level (or lower) are output. For example, message level also outputs message
with info, warning, and error levels.  

