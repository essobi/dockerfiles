# Dockerfile for kiwi bulk loader  
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
postgresql-client-common \  
postgresql-client-9.5 \  
&& apt-get clean  
  
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

