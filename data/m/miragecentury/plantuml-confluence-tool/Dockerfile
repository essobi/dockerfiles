FROM python  
  
RUN apt-get update  
RUN apt-get install nodejs default-jre npm -y  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install node-plantuml -g  
RUN export PYTHONUNBUFFERED=1  
RUN export PYTHONPATH="$PWD/k-arch-tool:$PYTHONPATH"  

