FROM ubuntu:14.04  
MAINTAINER Milo van der Linden <milo@dogodigi.net>  
  
ENV CARTO_ENV development  
ENV CARTO_DB_PREFIX cartodb_dev_user_  
ENV CARTO_DB_USER_PREFIX development_cartodb_user_  
ENV DB_HOST db  
ENV DB_PORT 5432  
ENV DB_USER postgres  
  
ENV REDIS_HOST redis  
ENV REDIS_PORT 6379  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends apt-utils make g++ git-core \  
ca-certificates \  
libicu-dev \  
gdal-bin libgdal1-dev libgdal-dev libproj-dev \  
nodejs nodejs-legacy npm && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git config --global user.email docker@codefor.nl  
RUN git config --global user.name "CodeForNL docker"  
  
# ogr2ogr2 static build, see https://github.com/CartoDB/cartodb/wiki/How-to-
build-gdal-and-ogr2ogr2  
RUN cd /opt && git clone https://github.com/OSGeo/gdal ogr2ogr2 && cd ogr2ogr2
&& \  
git remote add cartodb https://github.com/cartodb/gdal && git fetch cartodb &&
\  
git checkout trunk && git pull origin trunk && \  
git checkout upstream && git merge -s ours --ff-only origin/trunk && \  
git checkout ogr2ogr2 && git merge -s ours upstream -m "Merged it" && \  
cd ogr2ogr2 && ./configure --disable-shared && make -j 4 && \  
cp apps/ogr2ogr /usr/bin/ogr2ogr && ln -s /usr/bin/ogr2ogr /usr/bin/ogr2ogr2
&& rm -rf /opt/ogr2ogr2 /root/.gitconfig  
  
RUN git clone \--depth 1 --branch master https://github.com/cartodb/cartodb-
sql-api.git /cartodb-sql-api  
RUN mkdir -p /cartodb-sql-api/logs  
RUN mkdir -p /cartodb-sql-api/config/environments  
RUN mkdir -p /tmp  
WORKDIR /cartodb-sql-api  
RUN npm install  
  
# Add config  
COPY docker.js /cartodb-sql-api/config/environments/docker.js  
# Add image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 8080  
CMD ["/run.sh"]  

