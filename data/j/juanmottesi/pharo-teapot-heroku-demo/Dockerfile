FROM juanmottesi/pharo-docker  
  
WORKDIR /opt/pharo  
  
ADD ./*.st ./  
ADD ./*.sh ./  
  
#Installing st  
RUN ./pharo Pharo.image st --save --quit ./teapot.st  
  
# Create heroku port file  
RUN touch port.txt  
  
# Expose port - only work locally  
EXPOSE 5000  
#Start teapot server  
CMD ["bash","./start.sh"]  
  
RUN echo "End"  

