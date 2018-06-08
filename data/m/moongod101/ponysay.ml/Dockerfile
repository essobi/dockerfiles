FROM node  
  
RUN apt-get update -y && \  
apt-get install openssl python3 texinfo unzip -y && \  
wget -O ponysay.zip http://github.com/erkin/ponysay/archive/master.zip && \  
unzip ponysay.zip && cd ponysay-master && \  
./setup.py install --freedom=partial && \  
apt-get remove openssl texinfo -y && \  
rm -rf /ponysay.zip /ponysay-master /usr/lib/python*/__pycache__/*.pyc 2>
/dev/null  
  
WORKDIR /app  
  
COPY package.json .  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 3000  
CMD [ "npm", "start" ]

