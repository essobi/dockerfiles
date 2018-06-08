FROM node  
RUN mkdir /app  
RUN npm install -g @google-cloud/functions-emulator  
RUN apt-get update \  
&& apt-get -y install vim \  
&& rm -rf /var/lib/apt/lists/*  
WORKDIR /app  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-145.0.0-linux-x86_64.tar.gz \  
&& tar -zxvf google-cloud-sdk-145.0.0-linux-x86_64.tar.gz \  
&& ./google-cloud-sdk/install.sh \  
&& /app/google-cloud-sdk/bin/gcloud components install alpha beta gsutil  
ADD config.json /root/.config/configstore/@google-cloud/functions-
emulator/config.json  
  
CMD ["sh", "-c", "tail -f /dev/null"]  
EXPOSE 8010  

