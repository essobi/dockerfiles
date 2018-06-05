FROM node:8  
MAINTAINER Jean-Christophe Hoelt <hoelt@fovea.cc>  
  
# Create non-priviledged user  
RUN useradd app -d /home/app  
WORKDIR /home/app/code  
RUN chown -R app /home/app  
USER app  
  
# npm install  
COPY package.json /home/app/code/package.json  
RUN npm install  
  
# copy browser code && build a bundle  
RUN mkdir /home/app/code/web  
COPY web/js /home/app/code/web/js  
COPY web/libs /home/app/code/web/libs  
RUN (cd web && ../node_modules/.bin/browserify \  
\--transform [ babelify --presets [ es2017 react ] ] \  
\--transform brfs \  
\--outfile bundle.js \  
js/entrypoint.js)  
COPY web/css /home/app/code/web/css  
COPY web/images /home/app/code/web/images  
COPY web/index.html /home/app/code/web/index.html  
  
# copy server code  
COPY server/ /home/app/code/server/  
COPY index.js config.js README.md /home/app/code/  
  
# export stuff  
ENV ADMIN_USERNAME=admin  
ENV ADMIN_PASSWORD=admin  
ENV VIRTUAL_CURRENCY_CURRENCY_CODES=  
  
# run  
EXPOSE 8000  
CMD node index.js  

