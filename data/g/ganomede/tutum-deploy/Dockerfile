FROM node:0.10.33-slim  
EXPOSE 8000  
MAINTAINER Jean-Christophe Hoelt <hoelt@fovea.cc>  
  
RUN apt-get update && apt-get install -y python-pip && pip install tutum && rm
-rf /var/lib/apt/lists/*  
  
RUN useradd app -d /home/app  
WORKDIR /home/app/code  
COPY package.json /home/app/code/package.json  
RUN chown -R app /home/app  
  
USER app  
RUN npm install  
  
COPY .eslintrc .eslintignore Makefile index.js run.sh ganomede /home/app/code/  
COPY tests /home/app/code/tests  
COPY js /home/app/code/js  
COPY scripts /home/app/code/scripts  
  
USER root  
RUN chown -R app /home/app  
  
WORKDIR /home/app/code  
USER app  
RUN make  
  
# Deployment token (to keep very secret)  
ENV DEPLOY_TOKEN="" \  
TUTUM_USER="" \  
TUTUM_APIKEY="" \  
STORMPATH_API_ID="" \  
STORMPATH_API_SECRET="" \  
STORMPATH_APP_NAME="TestApp" \  
GANOMEDE_TAG="latest" \  
CHALLENGES_TYPE="" \  
CHALLENGES_INTERVAL="" \  
GAME_SERVERS_URL="" \  
API_SECRET="" \  
CDN_HOST="" \  
DBID="" \  
DBTAGS="" \  
CPID1="" \  
CPTAGS1="" \  
CPID2="" \  
CPTAGS2="" \  
CPID3="" \  
CPTAGS3="" \  
CPID4="" \  
CPTAGS4="" \  
CPID5="" \  
CPTAGS5="" \  
CPID6="" \  
CPTAGS6="" \  
CPID7="" \  
CPTAGS7="" \  
CPID8="" \  
CPTAGS8=""  
CMD ./run.sh  

