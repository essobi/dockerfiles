FROM softbrix/shatabang-base:latest  
MAINTAINER Andreas Sehr  
  
ENV SERVER_SALT 6548ee70d7d258e34eaf4daf9d8c30214bf8163e  
ENV ADMIN_HASH
98962591ddd626a5857a82e4ad876975e71e1a9cf586ff4cc4c57eb453d172cd  
ENV BASE_URL /  
ENV BUILD_BASE_URL /replacemeurl/  
ENV PORT 3000  
#Install source  
# TODO: git checkout  
COPY *.json /usr/src/shatabang/  
COPY *.lock /usr/src/shatabang/  
COPY client/*.json /usr/src/shatabang/client/  
  
WORKDIR /usr/src/shatabang  
  
# Install app dependencies  
RUN yarn install --production --non-interactive --pure-lockfile && \  
# Build client  
cd client && \  
npm install  
  
COPY . .  
  
# Create empty config  
RUN echo '{}' > config_server.json && \  
chmod +x docker_start.sh && \  
# Build client  
npm run build_client  
  
# USER node  
EXPOSE 3000  
CMD ./docker_start.sh && sh  

