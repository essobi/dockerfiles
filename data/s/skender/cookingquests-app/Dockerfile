FROM node:latest  
RUN apt-get update && apt-get install -y unzip  
ADD https://github.com/CookingQuest/app/archive/master.zip /repo/repo.zip  
WORKDIR /repo  
RUN unzip repo.zip  
WORKDIR /repo/app-master  
RUN yarn && yarn run build  
RUN mv dist /dist && rm -rf /repo  
CMD ["cp", "-a", "/dist/.", "/app/"]

