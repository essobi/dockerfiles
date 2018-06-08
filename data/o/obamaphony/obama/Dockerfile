FROM alpine:3.4  
RUN echo '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories  
  
RUN apk add --no-cache git nodejs python py-pip g++ make py-numpy@testing  
RUN pip install nltk  
  
ENV USERNAME docker  
  
RUN addgroup -S $USERNAME \  
&& adduser -S $USERNAME \  
&& adduser $USERNAME $USERNAME  
  
RUN git clone https://github.com/ObamaPhony/node-app.git /docker/app  
RUN git clone https://github.com/ObamaPhony/speech-analysis.git
/docker/analysis  
RUN git clone https://github.com/ObamaPhony/speech-generator.git
/docker/generator  
RUN ln -s ../analysis/speech-analysis.py /docker/app/bin/analyse  
RUN ln -s ../generator/speech-generator.py /docker/app/bin/generate  
  
WORKDIR /docker/app  
RUN npm install --production  
  
RUN apk del --no-cache --rdepends git py-pip g++ make  
RUN rm -rf ~/.cache ~/.npm ~/.node-gyp  
  
RUN chown -R $USERNAME:$USERNAME /docker  
USER $USERNAME  
  
EXPOSE 8080  
CMD ["npm", "start"]  

