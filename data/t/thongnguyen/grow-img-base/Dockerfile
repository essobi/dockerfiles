FROM grow/growsdk  
RUN pip install --upgrade grow  
  
# Install NodeJS v8.x  
RUN apt-get install curl  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN apt-get install -y nodejs  
  
# Install Yarn  
RUN npm install -g yarn  
  
# Install Bower  
RUN yarn global add bower  
RUN echo "{ \"allow_root\": true }" > $HOME/.bowerrc  
  
# Install Gulp  
RUN yarn global add gulp  
  
ENTRYPOINT ["grow"]

