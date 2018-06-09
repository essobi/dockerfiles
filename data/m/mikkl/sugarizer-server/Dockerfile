FROM node:5.7.1-slim  
RUN mkdir /sugarizer-repo  
WORKDIR /sugarizer-repo  
RUN apt-get update  
RUN apt-get install git -y  
RUN git clone https://github.com/llaske/sugarizer.git  
RUN rm -fr sugarizer/.git  
WORKDIR /sugarizer-repo/sugarizer/server  
RUN sed -i 's/localhost/mongodb/g' /sugarizer-
repo/sugarizer/server/sugarizer.ini  
RUN sed -i 's/27018/27017/g' /sugarizer-repo/sugarizer/server/sugarizer.ini  
RUN npm install  
ENTRYPOINT ["node", "/sugarizer-repo/sugarizer/server/sugarizer.js"]  

