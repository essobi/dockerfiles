#see dockerfile best practices  
#TODO:  
#apt-get sqlite3  
#use .dockerignore  
#options to activate only certain services  
#path to config.js, path to sqlite file  
# node.js base image  
# already contains: npm, git, python  
FROM node  
  
# install statsd  
RUN git clone https://github.com/etsy/statsd.git  
  
# install statsd-sqlite-backend  
RUN git clone https://github.com/TiemeTogola/statsd-sqlite-backend.git  
RUN mkdir -p /stastd/node_modules \  
&& npm install --prefix /statsd statsd-sqlite-backend/  
  
# install sqlite-timeseries-dashboard  
RUN git clone https://github.com/TiemeTogola/sqlite-timeseries-dashboard.git  
RUN npm install sqlite-timeseries-dashboard/  
  
#RUN pip install metric source  
# local files to include in the image  
ADD config.js /statsd/config.js  
ADD start-services /start-services  
# empty sqlite database  
RUN touch test.sqlite  
  
# ports available from other containers  
# use publish to make available from anywhere  
# eg: docker run -p 8125:8125/udp  
# 8125: statsd, 8126: statds admin, 8000: sqlite-timeseries-dashboard  
EXPOSE 8125/udp  
EXPOSE 8126/tcp  
EXPOSE 8000/tcp  
  
# launch services  
CMD ./start-services  

