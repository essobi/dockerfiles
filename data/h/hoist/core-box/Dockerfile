FROM iojs:1.8  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup --gid 1001 hoist && adduser --system --uid 1003 --ingroup hoist
--disabled-password hoist && usermod -a -G staff hoist && chown -R root:staff
/usr/local/  
  
#create and set the working directory  
RUN mkdir -p /usr/src/app/coverage && mkdir /home/hoist/.npm  
  
#sort out permissions  
RUN chown -R hoist:hoist /home/hoist/.npm && chown -R hoist:hoist /usr/src/app  
  
#don't include .npm cache in final image  
VOLUME /home/hoist/.npm  
  
#switch to the hoist user  
USER hoist  
  
WORKDIR /usr/src/app  
  
#only show warnings for npm  
ENV NPM_CONFIG_LOGLEVEL=warn  
  
#install global packages  
RUN npm install npm -g  
RUN npm install mongoose mongoose-data-migrate nodemon gulp bson babel bunyan-
hub bunyan-sub -g

