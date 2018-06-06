# Use an official Python runtime as a parent image  
FROM champsys/ubuntu-16-nodejs  
  
# Set the working directory to /app  
WORKDIR /home  
  
# Copy the current directory contents into the container at /app  
ADD . /home  
  
# Install any needed packages needed here  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y python-pip  
RUN pip install awscli --upgrade --user  
RUN mkdir /root/.aws  
RUN touch /root/.aws/credentials  
RUN touch /root/.aws/config  
RUN echo "[default]" >> /root/.aws/credentials  
RUN echo "aws_access_key_id = AKIAIV5WMJ2KUG7JMCEA" >> /root/.aws/credentials  
RUN echo "aws_secret_access_key = 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" >>
/root/.aws/credentials  
RUN echo "[default]" >> /root/.aws/config  
RUN echo "region = ap-south-1" >> /root/.aws/config  
RUN echo "output = text" >> /root/.aws/config  
  
# Make port 3000 available to the world outside this container  
EXPOSE 3000  
# Define environment variable  
ENV NODE_ENV=staging  
  
ENV MONGO_DB_URI=mongodb://champsys-logging-
adming:7lAUPdBvypQaV7Sc@cluster0-shard-00-00-lmcnk.mongodb.net:27017,cluster0-shard-00-01-lmcnk.mongodb.net:27017,cluster0-shard-00-02-lmcnk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin  
  
ENV SEED_IMPORT_ENABLED=false  
ENV RESET_ALL_TABLE=false  
ENV SEED_ALL_BASE_PRODUCTS=false  
ENV SEED_BASE_PRODUCT_TEMPLATE=false  
ENV SEED_TAG=false  
ENV SEED_OPTION=false  
ENV SEED_COUNTRY=false  
ENV SEED_USER=false  
ENV SEED_TEAM=false  
  
ENV SEED_OUTFIT=false  
ENV NUMBER_OF_OUTFIT=5  
ENV SEED_ORDERABLE=false  
ENV NUMBER_OF_ORDERABLE=10  
ENV SEED_DESIGN=false  
ENV SEED_ORDER=false  
ENV SEED_ORDER_ITEM=false  
ENV SEED_REVISION=false  
ENV SEED_SHIPPING=false  
ENV SEED_ADDRESS=false  
  
ENV LIVE_DOTNET_URL=http://custom.champ-sys.com:9090/csservice.asmx?WSDL  
ENV LIVE_DOTNET_APP=Altitude  
ENV LIVE_DOTNET_PASSWORD=PhErere2ez8CReTR  
ENV LIVE_DOTNET_ORDER_ID=AU-00516-18  
ENV LIVE_DOTNET_ORDER_FORM_TYPE=2  
#ENV LIVE_DOTNET_LOG=  
#ENV LIVE_DOTNET_LANGUAGE_ID=  
ENV DOTNET_URL=http://testcustom.champ-sys.com:9090/csservice.asmx?WSDL  
ENV DOTNET_APP=Altitude  
ENV DOTNET_PASSWORD=PhErere2ez8CReTR  
ENV DOTNET_ORDER_ID=AU-00392-17  
ENV LIVE_DOTNET_ORDER_FORM_TYPE=2  
#ENV DOTNET_LOG=  
#ENV DOTNET_LANGUAGE_ID=  
ENV POSTGRES_DATABASE=store_staging  
ENV POSTGRES_HOST=champsys-store-staging.cww7j8gxe4xj.ap-
south-1.rds.amazonaws.com  
ENV POSTGRES_USERNAME=champsys  
ENV POSTGRES_PASSWORD=champsysstore  
ENV POSTGRES_PORT=5432  
ENV AWS_ACCESS_KEY=AKIAIV5WMJ2KUG7JMCEA  
ENV AWS_SECRET_KEY=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  
  
# Install project dependents  
RUN ln -sf /root/.nvm/versions/node/v8.10.0/bin/node /usr/bin/node  
RUN ln -sf /root/.nvm/versions/node/v8.10.0/bin/npm /usr/bin/npm  
RUN ln -sf /root/.local/bin/aws /usr/bin/aws  
RUN npm install  
RUN npm run build-prod  
RUN cd client/dist  
RUN aws s3 sync ./client/dist/ s3://champsys-storefront/ --delete  
RUN cd /home  
RUN aws cloudfront create-invalidation --distribution-id EDMTM83FP9RJN --paths
/\\*  
  
# Run app.py when the container launches  
CMD node server/app.js  

