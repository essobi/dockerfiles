# Dockerfile  
# The FROM directive sets the Base Image for subsequent instructions  
FROM node  
RUN useradd -ms /bin/bash fresh  
  
COPY ./project /project  
  
COPY ./install.meteor.com /project/  
RUN chmod +x /project/install.meteor.com  
  
RUN chown -R fresh:root /project  
RUN chown -R fresh:root /usr/bin  
  
USER fresh  
WORKDIR /project  
  
ENV MONGO_URL mongodb://data-mongo-docker.fresh:27017  
#RUN curl https://install.meteor.com/ | sh  
RUN ./install.meteor.com  
RUN cp "/home/fresh/.meteor/packages/meteor-tool/1.4.2_6/mt-
os.linux.x86_64/scripts/admin/launch-meteor" /usr/bin/meteor  
  
RUN meteor npm install  
  
# Error: EXDEV: cross-device link not permitted  
# RUN mv /project/.meteor/local/build /project/.meteor/local/build-garbage-
uawuya  
CMD meteor run  
  
#Expose the port  
EXPOSE 3000  

