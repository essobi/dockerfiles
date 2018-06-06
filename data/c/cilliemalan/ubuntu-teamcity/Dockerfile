#sudo docker run -dt --name teamcity_server -p 80:80 cilliemalan/ubuntu-
teamcity  
FROM ubuntu  
  
MAINTAINER Cillié Malan <cilliemalan@gmail.com>  
  
WORKDIR /work/  
  
#add some files  
ADD database* nginx* postgres* teamcity* run.sh /work/  
  
#teamcity data directory  
ENV TEAMCITY_DATA_PATH=/data/teamcity  
  
#run the install scripts  
RUN ["/bin/bash", "teamcity-install.sh"]  
RUN ["/bin/bash", "postgres-install.sh"]  
RUN ["/bin/bash", "nginx-install.sh"]  
  
#mount some paths  
VOLUME ["data/postgres", "data/teamcity"]  
  
#expose port 80  
EXPOSE 80  
#run stuff  
CMD ["/bin/bash", "run.sh"]  

