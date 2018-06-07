FROM node:7.4.0  
MAINTAINER JerryZGY  
  
# 1. Download & install Meteor  
RUN curl -SL https://install.meteor.com/ -o /tmp/meteor.sh \  
&& sh /tmp/meteor.sh \  
&& rm /tmp/meteor.sh  
  
# 2. Create user  
RUN useradd meteor -G staff -m -s /bin/bash  
WORKDIR /home/meteor  
  
# 3. Create workdir  
RUN mkdir -p /home/meteor/src  
  
# 4. Copy source project  
COPY src /home/meteor/src  
  
# 5. Change user  
RUN su - meteor  
  
# 6. Install NPM modules  
RUN cd /home/meteor/src \  
&& meteor npm install --production \  
&& export LC_ALL=C  
  
# 7. Run Meteor  
EXPOSE 3000  
CMD [ "meteor" ]

