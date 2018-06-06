FROM mongo  
  
WORKDIR data/courses_db/  
  
# Modify child mongo to use /data/courses_db as dbpath (because /data/db wont
persist the build)  
RUN echo "dbpath = /data/courses_db" > /etc/mongodb.conf \  
&& chown -R mongodb:mongodb /data/courses_db  
  
COPY scripts/ scripts/  
  
RUN mongod --fork --logpath /var/log/mongodb.log --dbpath /data/courses_db
--smallfiles \  
&& CREATE_FILES=/data/courses_db/scripts/*_create.js \  
&& for f in $CREATE_FILES; do mongo 127.0.0.1:27017 $f; done \  
&& INSERT_FILES=/data/courses_db/scripts/*_insert.js \  
&& for f in $INSERT_FILES; do mongo 127.0.0.1:27017 $f; done \  
&& mongod --dbpath /data/courses_db --shutdown \  
&& chown -R mongodb /data/courses_db  
  
# Make the new dir a VOLUME to persists it  
VOLUME /data/courses_db  
  
CMD ["mongod", "--config", "/etc/mongodb.conf", "--smallfiles"]

