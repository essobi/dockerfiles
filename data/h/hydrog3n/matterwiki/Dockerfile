FROM xataz/node:lts  
  
LABEL description="Matterwiki on alpine" \  
tags="latest" \  
maintainer="hydrog3n <https://github.com/hydrog3n>"  
  
RUN BUILD_DEPS="git \  
ca-certificates" \  
&& apk add -U ${BUILD_DEPS}  
  
RUN git clone https://github.com/matterwiki/matterwiki \  
&& cd /matterwiki  
  
WORKDIR /matterwiki  
  
COPY ./knexfile.js /matterwiki/  
  
RUN npm install mysql \  
&& sed -i 's/\"sqlite3\"\:\ \"3\\.1\\.4\"\,//g' package.json \  
&& npm install \  
&& npm run build \  
&& apk del ${BUILD_DEPS} \  
&& rm -rf /var/cache/apk/*  
  
COPY startup /usr/local/bin/startup  
RUN chmod +x /usr/local/bin/startup  
  
EXPOSE 5000  
ENTRYPOINT ["/usr/local/bin/startup"]  
CMD ["npm", "start"]

