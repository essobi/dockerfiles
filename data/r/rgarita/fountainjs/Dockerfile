FROM node:6.10.2  
EXPOSE 3000  
RUN npm i -g gulp yo generator-fountain-webapp generator-fountain-react
generator-fountain-angular1 generator-fountain-angular2 && \  
npm cache clean  
  
VOLUME /usr/app/fountain  
WORKDIR /usr/app/fountain  
  
RUN useradd --create-home --shell /bin/bash fountain && \  
usermod -aG sudo fountain && \  
chown -R fountain:fountain /usr/app/fountain  
  
USER fountain  
  
CMD /bin/bash

