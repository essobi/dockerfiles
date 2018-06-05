# docker run --rm -p 9000:9000 silgon/strut  
FROM node:6.3-slim  
  
RUN wget https://github.com/tantaman/Strut/archive/master.tar.gz -O
./Strut.tar.gz \  
&& tar zxvf ./Strut.tar.gz \  
&& mv Strut-master strut \  
&& rm ./Strut.tar.gz  
  
WORKDIR /strut  
COPY replacement_files/package.json package.json  
COPY replacement_files/impress.html app/preview_export/impress.html  
COPY replacement_files/bespoke.html app/preview_export/bespoke.html  
COPY replacement_files/reveal.html app/preview_export/reveal.html  
COPY replacement_files/index.html app/index.html  
  
RUN npm install -g grunt-cli \  
&& npm install  
  
EXPOSE 9000  
CMD ["grunt", "server"]  

