# NAME: Captain Value Setter  
#  
# DESCRIPTION: This image sets hash values to redis.  
#  
# REQUIRED ENVS:  
# REDIS_HOST (ie. 127.0.0.1)  
# REDIS_PORT (ie. 6379)  
# REDIS_DATABASE (ie. 0)  
# REDIS_FIELDS_VALUES (ie. "update##!!0 restart##!!1")  
# REDIS_NAMESPACE (ie. "tds", : not allowed)  
# REDIS_APP_AVZONE (ie. "ht20")  
# REDIS_APP (ie. "elasticsearch_data")  
# REDIS_APP_HOST (ie. "ht20wrkprd001")  
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

