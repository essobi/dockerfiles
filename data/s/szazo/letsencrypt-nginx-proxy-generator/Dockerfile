FROM node:7  
# download and install simp_le  
RUN mkdir /simp_le  
RUN git -C /simp_le clone \--depth 1 https://github.com/zenhack/simp_le.git .  
  
WORKDIR /simp_le  
RUN ./bootstrap.sh  
RUN ./venv.sh  
  
# compile and add the app  
RUN mkdir /app  
WORKDIR /app  
  
ADD ./app/package.json /app/  
  
RUN npm install  
  
ADD ./app/tsconfig.json .  
ADD ./app/src ./src  
ADD ./app/entrypoint.sh .  
  
RUN `npm bin`/tsc  
RUN mkdir build/templates  
RUN cp -r src/templates/* build/templates  
  
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]  
  

