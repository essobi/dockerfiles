FROM efaille/java  
MAINTAINER Erick Faille "efaille@gmail.com"  
RUN update-ca-certificates -f  
  
RUN useradd -s /bin/bash -d /minecraft -m minecraft  
RUN chown -R minecraft:minecraft /minecraft  
  
ADD run.sh /  
RUN chmod 775 /run.sh  
CMD /run.sh  
  
VOLUME /minecraft  
WORKDIR /minecraft  
USER minecraft  
EXPOSE 25565  

