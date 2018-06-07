FROM hansd/node-phantom:0.10_1.9.8  
  
ENV METEOR_VERSION 1.1.0.2  
  
RUN curl -SL https://install.meteor.com/ -o /tmp/inst-meteor.sh ;\  
sed -i -e "s/^RELEASE=.*/RELEASE=\"\$METEOR_VERSION\"/" /tmp/inst-meteor.sh ;\  
sh /tmp/inst-meteor.sh ;\  
\  
rm -rf /var/lib/cache /var/lib/log /tmp/*  
  
RUN meteor update  

