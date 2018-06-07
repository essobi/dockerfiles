FROM jacobwgillespie/gui  
  
RUN \  
apt-get update -qq && \  
apt-get install -qy dolphin && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/*  
  
ADD /files/ /  
  
ENV APP_NAME=Dolphin  

