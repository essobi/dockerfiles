FROM node:5  
MAINTAINER anhln4@fsoft.com.vn  
  
RUN apt-get update && apt-get install -y git  
  
RUN npm install pm2 -g  
RUN npm install -g --unsafe-perm node-red  
  
RUN mkdir /setup  
WORKDIR /setup  
COPY . /setup  
  
VOLUME /root/.aws  
  
RUN apt-get install python2.7  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python2.7 get-pip.py  
RUN pip install awscli  
RUN pip install --upgrade awscli  
  
RUN git clone https://github.com/damphat/kv-bash.git  
RUN cp -ar ./kv-bash/kv-bash /usr/local  
RUN chmod +x /usr/local/kv-bash  
  
RUN cp /setup/include/* /usr/sbin/  
RUN chmod +x /usr/sbin/anl-*  
RUN mkdir /root/.node-red/  
RUN cd /root/.node-red/ && npm install node-red-contrib-http-auth0 && npm
install node-red-contrib-aws-sdk && npm install node-red-contrib-func-exec  
  
EXPOSE 1880  
ENTRYPOINT ["pm2"]  
CMD ["start", "node-red", "--no-daemon"]  

