FROM nginx  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# Install Linux Tools  
RUN apt-get update && apt-get -y install build-essential \  
htop \  
libcurl3 \  
libcurl3-dev \  
librecode0 \  
libsqlite3-0 \  
libxml2 \  
curl \  
wget \  
python \  
vim \  
nano \  
cron \  
git \  
unzip \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c \  
rsync \  
ruby-full \  
ca-certificates --no-install-recommends  
  
# Install Node JS  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get -y install nodejs  
  
# Install Node Tools  
RUN npm install -g bower  
RUN npm install -g gulp  
RUN npm install -g shipit-cli  
RUN npm install -g pm2  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

