# Dockerfile for USGS Triplifier  
FROM node:9  
MAINTAINER Blake Regalia <blake.regalia@gmail.com>  
  
# source code  
WORKDIR /src/app  
COPY . .  
  
# add PostgreSQL keys  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
# install packages  
RUN apt-get -y update \  
&& apt-get upgrade -y \  
&& apt-get install -yq \  
git \  
libpq-dev \  
postgresql-client-common \  
postgresql-client-9.5 \  
&& apt-get clean  
  
# download GDAL 2  
ENV GDAL_VERSION 2.1.3  
RUN mkdir -p /src/gdal2  
ADD http://download.osgeo.org/gdal/${GDAL_VERSION}/gdal-${GDAL_VERSION}.tar.gz
/src/gdal2  
  
# install GDAL 2  
RUN cd /src/gdal2 \  
&& tar -xvf gdal-${GDAL_VERSION}.tar.gz \  
&& cd gdal-${GDAL_VERSION} \  
&& ./configure --with-pg --with-curl \  
&& make \  
&& make install \  
&& ldconfig \  
&& rm -Rf /src/gdal2/*  
  
# special branch of graphy  
RUN npm i -g gulp  
RUN cd /src/ \  
&& git clone -b data_format https://github.com/blake-regalia/graphy.js.git
graphy \  
&& cd graphy \  
&& npm i \  
&& gulp \  
&& npm link  
  
# install software  
RUN npm i \  
&& npm link graphy  
  
# entrypoint  
ENTRYPOINT ["npm", "run"]  
CMD ["all"]  

