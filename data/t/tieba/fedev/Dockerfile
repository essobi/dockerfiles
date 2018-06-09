FROM ubuntu  
MAINTAINER liye04@baidu.com  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
wget \  
php5 \  
php5-cli \  
subversion \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm i -g \  
fis \  
yo \  
generator-surf \  
generator-mis \  
grunt \  
grunt-cli \  
bower \  
&& npm cache clear  
  
RUN echo "alias bower='bower --allow-root'" >> /root/.bashrc  
  
CMD ["/bin/bash"]  

