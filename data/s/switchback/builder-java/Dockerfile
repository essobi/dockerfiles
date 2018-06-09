FROM switchback/builder  
  
RUN apt-get update && \  
apt-get install -y openjdk-8-jdk maven && \  
rm -rf /var/lib/apt/lists/*  
  
# add script to run  
ADD *.sh /usr/local/bin/  
  
# set working directory  
WORKDIR /var/workspace  
  
# run  
CMD /bin/bash /usr/local/bin/run.sh  

