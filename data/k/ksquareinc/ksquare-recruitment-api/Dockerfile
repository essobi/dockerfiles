FROM node:5  
# App  
ADD . /  
  
# Install app dependencies  
RUN npm install  
  
# ENV VARIABLES  
ENV JWT_SECRET=~/K5qU4r3_App@2016/~.  
ENV DB_URI=mongodb://ds023418.mlab.com:23418/ksquare_recruitment  
ENV
DB_OPTIONS='{"db":{"native_parser":true},"server":{"poolSize":5,"socketOptions":{"keepAlive":300000,"connectTimeoutMS":30000}},"user":"ksquareinc","pass":"K5qU4r3"}'  
ENV
SENDGRID_API_KEY=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  
  
# Expose port 9001  
EXPOSE 9001  
# Init Server  
CMD npm run serve

