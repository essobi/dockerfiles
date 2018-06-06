#  
# base image  
#  
FROM amazon/aws-codebuild-local AS base  
  
#  
# add https?_proxy environment variables to docker-compose.yml  
#  
FROM perl:5.26 AS build  
  
COPY add_env_proxy.pl /root  
COPY \--from=base /LocalBuild/agent-resources/docker-compose.yml /root/docker-
compose.src.yml  
RUN cpanm YAML::Tiny \  
&& perl /root/add_env_proxy.pl < /root/docker-compose.src.yml > /root/docker-
compose.yml  
  
#  
# final image  
#  
FROM amazon/aws-codebuild-local  
  
COPY \--from=build /root/docker-compose.yml /LocalBuild/agent-
resources/docker-compose.yml  

