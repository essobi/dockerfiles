FROM nginx:latest  
RUN apt-get update && apt-get install -y unzip  
ADD https://github.com/CookingQuest/nginx/archive/master.zip /repo/repo.zip  
WORKDIR /repo  
RUN unzip repo.zip  
RUN mv -f nginx-master/*.conf /etc/nginx

