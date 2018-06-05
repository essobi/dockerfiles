from ubuntu:16.04  
RUN cd /tmp  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN apt update  
RUN apt install -y python3 python3-pip mongodb-org -y  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
ADD . /opt/app  
RUN pip3 install -r /opt/app/req.txt  
RUN echo "/usr/bin/mongod --quiet --config /etc/mongod.conf &" > /startup.sh  
RUN echo "mongoimport --db paranuaran --collection people --drop --file
/opt/app/resources/mongo/people.json" >> /startup.sh  
RUN echo "mongoimport --db paranuaran --collection food --drop --file
/opt/app/resources/mongo/food.json" >> /startup.sh  
RUN echo "mongoimport --db paranuaran --collection companies --drop --file
/opt/app/resources/mongo/companies.json" >> /startup.sh  
RUN echo "python3 /opt/app/app.py" >> /startup.sh  
RUN chmod a+x /startup.sh  
EXPOSE 5000  
CMD /startup.sh

