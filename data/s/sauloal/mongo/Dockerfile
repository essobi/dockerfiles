# TO BUILD docker build -t sauloal/mongo .  
# TO RUN docker run -d -p 27017:27017 -p 28017:28017 --name="sauloal_mongo"
sauloal/mongo  
# TO UPLOAD while true; do docker push sauloal/mongo; echo $?; if [ $? == "0"
]; then exit 0; fi; done  
  
#docker build -t robinvdvleuten/mongo < Dockerfile_robinvdvleuten_mongo  
#docker build -t sauloal/mongo < Dockerfile_robinvdvleuten_mongo  
  
#BASED ON robinvdvleuten/mongo  
  
FROM sauloal/supervisor  
  
  
# Add 10gen official apt source to the sources list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/10gen.list  
  
# Hack for initctl not being available in Ubuntu  
#RUN dpkg-divert --local \--rename --add /sbin/initctl  
#RUN ln -s /bin/true /sbin/initctl  
  
# Install MongoDB  
RUN apt-get update  
RUN apt-get install mongodb-10gen  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
  
ADD mongo.service.conf /etc/supervisor/conf.d/mongo.service.conf  
ADD run.sh /run.sh  
  
#mongo port  
EXPOSE 27017  
  
#mongo rest port  
EXPOSE 28017  
  
#ENTRYPOINT ["usr/bin/mongod"]  
  
#CMD "supervisor -c /etc/supervisor.conf"  
CMD /bin/bash /run.sh  

