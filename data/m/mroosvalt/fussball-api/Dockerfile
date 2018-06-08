FROM ubuntu  
  
RUN apt-get update --fix-missing  
RUN apt-get install -yq curl  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash - && \  
apt-get install -y nodejs  
  
#VOLUME ./app:/nodeapp  
ADD app /nodeapp  
WORKDIR /nodeapp  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
npm install -g nodemon mocha supervisor  
CMD ["nodemon", "/app/app.js"]

