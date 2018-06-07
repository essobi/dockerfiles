FROM docker  
  
#RUN apt-get update && apt-get install -y \  
# apt-transport-https \  
# ca-certificates \  
# curl \  
# gnupg2 \  
# software-properties-common \  
# curl  
#  
#RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  
#RUN add-apt-repository \  
# "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release;
echo "$ID") \  
# $(lsb_release -cs) \  
# stable"  
#RUN apt-get update && apt-get install docker-ce -y  
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
COPY kill.sh /bin/kill.sh  
  
RUN chmod +x /bin/kill.sh  
  
ENV WAIT 5  
  
ENTRYPOINT kill.sh  

