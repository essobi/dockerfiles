FROM xueshanf/awscli  
MAINTAINER Xueshan Feng <sfeng@stanford.edu>  
  
# See https://github.com/xueshanf/docker-aws-ses/blob/master/README.md  
# Add our script  
ADD aws-ses.sh /aws-ses.sh  
RUN chmod 755 /aws-ses.sh  
CMD ["/aws-ses.sh"]  

