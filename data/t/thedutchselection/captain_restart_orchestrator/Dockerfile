# NAME: Captain Restart Orchestrator  
#  
# DESCRIPTION: This image sets the restart keys for the containers that have
the need_restart key set. By default it  
# sets 1 restart key at once, except for the exception keys.  
#  
# REQUIRED ENVS:  
# REDIS_HOST (ie. 127.0.0.1)  
# REDIS_PORT (ie. 6379)  
# REDIS_DATABASE (ie. 0)  
# REDIS_NAMESPACE (ie. "tds", : not allowed)  
# APP_EXCEPTIONS_AMOUNTS (ie. "price_comparator_nl_telecom:##!!2
insights:##!!4")  
# REFRESH_TIME (in seconds, ie. 15)  
#  
# OPTIONAL ENVS:  
# REDIS_PASSWORD (ie. abcdabcd)  
#  
# OTHER:  
  
FROM thedutchselection/captain_services_base:latest  
MAINTAINER Gerard Meijer <g.meijer@thedutchselection.com>  
  
ADD files/scripts /usr/local/bin  
  
RUN chmod +x /usr/local/bin/*  
  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/run.sh"]

