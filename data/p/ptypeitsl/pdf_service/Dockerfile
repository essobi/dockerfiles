FROM node:8-alpine  
LABEL Author="Kristoffer Andersen <ka@ptype.dk>"  
  
RUN apk add --update --no-cache \  
libgcc libstdc++ libx11 glib libxrender libxext libintl \  
libcrypto1.0 libssl1.0 \  
ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family  
  
# on alpine static compiled patched qt headless wkhtmltopdf (47.2 MB)  
# compilation takes 4 hours on EC2 m1.large in 2016 thats why binary  
COPY . /app  
RUN ln -s /app/wkhtmltopdf /bin && chmod +x /app/wkhtmltopdf  
WORKDIR /app  
  
# Setup node app environment  
RUN npm install  
  
CMD npm run serve

