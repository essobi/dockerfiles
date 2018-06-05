FROM mhart/alpine-node:6  
ENV PORT 8080  
EXPOSE ${PORT}  
  
RUN mkdir -p /srv/app/  
WORKDIR /srv/app/  
  
# Install global dependencies  
RUN apk add --no-cache make gcc g++ python  
  
# Add package.json first so that the docker image build can use  
# the cache as long as contents of package.json hasn't changed.  
COPY package.json /srv/app/  
RUN npm install  
  
# Copy source in the last step as the source might change the most.  
COPY . /srv/app/  
  
VOLUME "/srv/app/data/"  
  
CMD ["npm", "start"]

