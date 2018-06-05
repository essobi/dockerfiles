FROM node  
  
EXPOSE 80  
VOLUME /usr/src  
  
# download and install hugo  
ENV HUGO_VERSION 0.35  
RUN wget -q -O /tmp/hugo.tgz
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
\  
&& tar xzf /tmp/hugo.tgz -C /opt \  
&& test -f /opt/hugo \  
&& ln -s /opt/hugo /usr/bin/hugo \  
&& rm /tmp/hugo.tgz  
  
# setup gulp build  
RUN mkdir /usr/build  
WORKDIR /usr/build  
  
RUN npm install -g gulp  
  
ONBUILD COPY package.json /usr/build/  
ONBUILD RUN npm install  
  
ONBUILD COPY gulpfile.js /usr/build/  
  
# create entrypoint  
COPY entrypoint.sh /usr/bin/  
RUN chmod +x /usr/bin/entrypoint.sh  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["server"]  

