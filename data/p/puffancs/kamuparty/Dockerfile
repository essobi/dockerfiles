FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y nginx  
ENV PARTY_NAME "Maradi Szegmentalis Pukkandurok"  
ENV COLOR "lightgreen"  
COPY start.sh /  
CMD ["/start.sh"]

