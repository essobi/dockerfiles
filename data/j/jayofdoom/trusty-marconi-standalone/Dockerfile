# Dockerfile for marconi-dev-env  
# Forked from https://github.com/bentwire/marconi-simple for Trusty support  
FROM jayofdoom/docker-ubuntu-14.04  
MAINTAINER Jay Faulkner <jay.faulkner@rackspace.com>  
  
# Add mongo repo, install mongodb + requirements  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
| \  
tee /etc/apt/sources.list.d/mongodb.list && \  
apt-get -y update && \  
apt-get -y install python-pip python-dev git mongodb-10gen gcc make netcat  
  
# Install marconi, wsgi server, tools  
RUN pip install -e git+https://github.com/openstack/marconi#egg=marconi
gunicorn  
  
# Install marconi configs  
ADD marconi.conf /etc/marconi/  
ADD doit.sh /  
  
# Open up the required ports for API access  
EXPOSE 80 443 27017  
CMD ["/doit.sh"]  
  

