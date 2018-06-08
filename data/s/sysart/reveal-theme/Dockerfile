FROM node:0.10  
RUN git clone https://github.com/hakimel/reveal.js.git  
RUN cd reveal.js && npm install  
RUN npm install -g grunt-cli  
ADD theme_images /reveal.js/theme_images  
ADD sysart.css /reveal.js/sysart.css  
WORKDIR /reveal.js/  
ENTRYPOINT ["grunt", "serve"]  
EXPOSE 8000  

