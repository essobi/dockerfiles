FROM ubuntu:14.04  
MAINTAINER Jonah Sullivan <jonah@thats.ninja>  
  
# Install Dependencies.  
RUN apt-get update && apt-get install -y libffi-dev libssl-dev pgpool2 python
python-dev python-pip  
RUN pip install Jinja2  
  
# Post Install Configuration.  
ADD bin/start-pgpool2 /usr/bin/start-pgpool2  
RUN chmod +x /usr/bin/start-pgpool2  
ADD conf/pcp.conf.template /usr/share/pgpool2/pcp.conf.template  
ADD conf/pgpool.conf.template /usr/share/pgpool2/pgpool.conf.template  
ADD conf/pool_hba.conf.template /etc/pgpool2/pool_hba.conf  
  
RUN touch /var/log/postgresql/pgpool_status && chown root:postgres
/var/log/postgresql/pgpool_status && chmod 0664
/var/log/postgresql/pgpool_status  
  
# Start the container.  
CMD start-pgpool2  

