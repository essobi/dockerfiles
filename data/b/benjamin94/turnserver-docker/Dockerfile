FROM ubuntu  
MAINTAINER Benjamin Faal  
  
RUN apt-get update -y  
RUN apt-get install -y gdebi-core  
  
COPY coturn_4.2.1.2-1_amd64.deb /coturn.deb  
RUN dpkg --force-all -i coturn.deb  
RUN apt-get -y -f install  
  
ENV SHARED_KEY FILL_KEY_IN  
  
RUN printf "verbose\nlt-cred-mech\nuser=$SHARED_KEY:$SHARED_KEY\nrest-api-
separator=-" > /etc/turnserver.conf  
  
EXPOSE 3478  
CMD turnserver  

