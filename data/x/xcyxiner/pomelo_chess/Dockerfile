FROM xcyxiner/lordofpomelo  
WORKDIR /usr/src/app  
RUN rm -rf /usr/src/app/*  
RUN git clone https://github.com/xcyxiner/chess.git  
ADD package.json /usr/src/app/chess/game-server/package.json  
ADD servers.json /usr/src/app/chess/game-server/config/servers.json  
ADD app.js /usr/src/app/chess/web-server/app.js  
RUN cd chess;sh npm-install.sh  
ADD gameserverstart.sh /usr/src/app/chess/game-server/gameserverstart.sh  
ENTRYPOINT cd /usr/src/app/chess/game-server/;sh gameserverstart.sh;cd
/usr/src/app/chess/web-server/;node app.js  

