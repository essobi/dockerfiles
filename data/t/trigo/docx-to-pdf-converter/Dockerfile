FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && \  
apt-get -yqq install apt-transport-https curl && \  
curl -SL https://deb.nodesource.com/setup_9.x | sudo -E bash - && \  
apt-get -yqq install nodejs  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" >>
/etc/apt/sources.list.d/yarn.list && \  
apt-get -qq update && \  
apt-get -yqq install yarn  
  
RUN apt-get -yqq install libreoffice libreoffice-writer ure libreoffice-java-
common libreoffice-core libreoffice-common openjdk-7-jre fonts-opensymbol
hyphen-fr hyphen-de hyphen-en-us hyphen-it hyphen-ru fonts-dejavu fonts-
dejavu-core fonts-dejavu-extra fonts-droid fonts-dustin fonts-f500 fonts-
fanwood fonts-freefont-ttf fonts-liberation fonts-lmodern fonts-lyx fonts-sil-
gentium fonts-texgyre fonts-tlwg-purisa && apt-get -q -y remove libreoffice-
gnome  
  
RUN adduser --home=/opt/libreoffice --disabled-password --gecos ""
\--shell=/bin/bash libreoffice  
  
ADD sofficerc /etc/libreoffice/sofficerc  
  
WORKDIR /app  
  
ADD package.json /app/package.json  
ADD yarn.lock /app/yarn.lock  
RUN npm install  
ADD . /app  
  
CMD ["yarn", "start"]  

