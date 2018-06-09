FROM node:4.3.1-slim  
ENV REFRESHED_AT 2016_03_21  
  
RUN wget https://github.com/thielCole/Strut/archive/master.tar.gz -O
./Strut.tar.gz \  
&& tar zxvf ./Strut.tar.gz \  
&& mv Strut-master Strut \  
&& rm ./Strut.tar.gz  
  
WORKDIR ./Strut  
  
RUN npm install -g grunt-cli \  
&& npm install  
  
EXPOSE 9000  
CMD ["grunt", "server"]  

