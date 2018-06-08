FROM node  
WORKDIR /usr/src/app  
RUN npm install gulp -g  
RUN git clone https://github.com/insolite/gitlab-time-report /usr/src/app  
RUN npm install && gulp sass  
ADD start.sh /start.sh  
CMD /start.sh  

