FROM ubuntu:14.04  
MAINTAINER dooros@posgrado.upv.es  
  
# Define a volume for the database  
VOLUME ["/data/db"]  
  
# install SSH  
RUN apt-get update && apt-get -y install openssh-server supervisor  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' |chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
# Install MongoDB  
RUN \  
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 &&
\  
sudo echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2
multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
sudo apt-get update && \  
sudo apt-get install -y mongodb-org  
RUN apt-get update  
  
# Install Node.js  
RUN apt-get install --yes curl  
RUN curl --silent --location https://deb.nodesource.com/setup_8.x | sudo -E
bash -  
RUN apt-get install --yes nodejs  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
# Open the ports  
EXPOSE 22 3000 27017  
# run services  
#CMD ["/usr/sbin/sshd", "-D"]  
#ENTRYPOINT ["/usr/sbin/sshd", "-D"]  
#CMD ["mongod"]  
CMD ["/usr/bin/supervisord"]  
  

