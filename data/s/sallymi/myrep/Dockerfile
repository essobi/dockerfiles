# Copyright IBM Corp, All Rights Reserved.  
#  
# SPDX-License-Identifier: Apache-2.0  
#  
FROM node:9.2 as build_js  
MAINTAINER haitao yue "hightall@me.com"  
# COPY package.json /  
RUN git clone https://github.com/hyperledger/cello.git && \  
cd /cello && \  
git checkout master && \  
mkdir /app && \  
cp -r /cello/src/* /app && \  
rm -rf /cello  
RUN cd /app/themes/vue/static && npm config set registry
'https://registry.npm.taobao.org' && \  
npm install --loglevel http && npm run build  
ENV PATH ${PATH}:/node_modules/.bin  
  
  
FROM hyperledger/cello-baseimage:x86_64-latest  
COPY \--from=build_js /app/themes/vue /app/themes/vue  
# use this in development  
CMD ["python", "dashboard.py"]  
  
# use this in product  
#CMD ["gunicorn", "-w", "128", "-b", "0.0.0.0:8080", "dashboard:app"]  

