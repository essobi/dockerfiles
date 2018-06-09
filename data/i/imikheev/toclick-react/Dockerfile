# You should always specify a full version here to ensure all of your
developers  
# are running the same version of Node.  
FROM nginx  
  
# Install packages, nodejs and npm  
RUN apt-get update \  
&& apt-get install -y curl \  
&& apt-get -y autoclean  
  
RUN apt-get -y install build-essential && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs  
  
# Remove the default nginx index.html  
RUN rm -rf /var/www/html/*  
RUN rm -rf /etc/nginx/conf.d/*  
  
# Install dependencies  
# COPY package.json package.json  
# RUN npm install  
# Copy all local files into the image and build production assets  
ADD . /app  
WORKDIR /app  
RUN npm install  
RUN npm run build --production  
  
# Copy the contents of the build directory over to the nginx web root  
# COPY /app/build /var/www/html/  
COPY toclick.conf /etc/nginx/conf.d/toclick.conf  
  
# Expose the public http port  
EXPOSE 80  
# Start server  
CMD ["nginx", "-g", "daemon off;"]  

