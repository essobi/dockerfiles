#  
# Controller  
#  
# Pull base image.  
FROM dockerfile/nodejs  
  
MAINTAINER Roberto Jimenez totemteleko@gmail.com  
  
# Move the controller app  
ADD web /web  
  
# Move run file.  
# Expose port  
EXPOSE 3000  
# Initial command  
CMD npm start /web/.

