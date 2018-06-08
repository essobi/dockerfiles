FROM openjdk:8  
RUN apt-get update && apt-get install -y git wget tar maven iceweasel fish  
  
ENV version IU-2018.1.3  
RUN wget https://download.jetbrains.com/idea/idea${version}.tar.gz &&\  
tar -xzf idea${version}.tar.gz && rm -f idea${version}.tar.gz  
  
ENV in_version IU-181.4892.42  
CMD idea-${in_version}/bin/idea.sh  
# CMD idea-IU-181.4892.42/bin/idea.sh  

