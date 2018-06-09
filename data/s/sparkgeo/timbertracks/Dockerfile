FROM sparkgeo/base  
  
RUN apt-get update && apt-get install -y --no-install-recommends
postgresql-9.4  
  
RUN mkdir -p /timbertracks  
RUN mkdir -p /timbertracks_logs && chmod 777 /timbertracks_logs  
WORKDIR /timbertracks_logs  
RUN touch timbertracks_dev.log && chmod 777 timbertracks_dev.log  
WORKDIR /timbertracks  
  
# Python packages  
ADD ./pnllog/requirements.txt ./requirements.txt  
RUN pip install --upgrade pip  
RUN pip install -r ./requirements.txt  
  
# NPM  
ADD ./pnllog/package.json ./package.json  
RUN npm install  
  
# Gulp, add file, don't build  
ADD ./pnllog/gulpfile.js /gulpfile.js  
  
# Gunicorn  
RUN groupadd webapps  
RUN useradd webapp -G webapps  
RUN mkdir -p /var/run/timbertracks/ && chmod -R 777 /var/run/timbertracks/  
  
# Nginx  
RUN rm /etc/nginx/sites-enabled/default && rm /etc/nginx/sites-
available/default  
ADD ./deploy/webapp.nginxconf /etc/nginx/sites-enabled/  
  
# Supervisor  
RUN mkdir -p /var/log/supervisor  
ADD ./deploy/supervisor_conf.d/nginx.conf /etc/supervisor/conf.d/  
ADD ./deploy/supervisor_conf.d/webapp.conf /etc/supervisor/conf.d/  

