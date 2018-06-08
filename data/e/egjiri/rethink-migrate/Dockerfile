FROM egjiri/node:8.9.3  
# Get vendor packages  
COPY package.json .  
COPY yarn.lock .  
RUN yarn  
  
# ========== Final Build Stage ==========  
FROM egjiri/node:8.9.3  
# Set arguments  
ARG RETHINK_MIGRATE_VERSION="1.3.1"  
# Set the working directory  
WORKDIR /data  
  
# Set the Volume mount point which will store the database.json config and
migrations  
VOLUME /data/rethinkdb  
  
# Copy the node modules from the previous build  
COPY \--from=0 node_modules node_modules  
  
# Install the rethink-migrate binary  
RUN yarn global add rethink-migrate@${RETHINK_MIGRATE_VERSION}  
  
# Start the rethink-migrate binrary referencing the config data in the Volume  
ENTRYPOINT ["rethink-migrate", "--root", "rethinkdb"]  

