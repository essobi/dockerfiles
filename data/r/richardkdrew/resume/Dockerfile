# DOCKER-VERSION 1.6.2  
#  
# Node.js Dockerfile  
#  
# https://github.com/richardkdrew/resume  
#  
FROM richardkdrew/nodejs  
  
MAINTAINER Richard Drew <richardkdrew@gmail.com>  
  
COPY *.json /resume/  
  
WORKDIR "/resume"  
  
RUN npm install  
  
EXPOSE 4000  
ENTRYPOINT ["node", "./node_modules/resume-cli/index.js"]  
CMD ["serve", "--theme", "elegant"]

