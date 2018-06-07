# NAME: Data  
#  
# DESCRIPTION: Image meant to hold persistant data from other containers. The
user and group on the data folder can be  
# set to the ones needed by the container(s) using the container from this
image. If GROUP_READABLE is set to 1, the  
# permissions on the directory will be 750, else they will be 700.  
#  
# REQUIRED ENVS:  
# DATA_DIRECTORY (ie. "/home/redis/db")  
# USER_ID (ie. "6379")  
# GROUP_ID (ie. "6379")  
#  
# OPTIONAL ENVS:  
# GROUP_READABLE (ie. "1")  
#  
# USAGE EXAMPLE: docker run --name redis_data -e
DATA_DIRECTORY="/home/redis/db" -e USER_ID="6379" -e GROUP_ID="6379"  
# -v /home/redis/db thedutchselection/data  
  
FROM busybox  
MAINTAINER Gerard Meijer <g.meijer@thedutchselection.com>  
  
ADD files/scripts /usr/local/bin  
  
ENTRYPOINT ["sh", "/usr/local/bin/run.sh"]

