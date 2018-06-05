FROM node:6.9.1  
MAINTAINER docker_user cain@cainplay.com  
RUN apt-get install -y git \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y yarn \  
&& git clone http://60.251.125.207:8888/demo/oview-web-demo.git \  
&& cd oview-web-demo \  
&& git checkout origin/demo_2016_1125 \  
&& yarn  
WORKDIR /oview-web-demo  
EXPOSE 80  
CMD ["yarn","start"]

