FROM node:5  
ADD . .  
  
RUN apt-get update && \  
apt-get install -y ruby ruby-dev gcc git rsync make && \  
gem install jekyll -v 3.1.6 && \  
npm install && \  
git clone
https://github.com/ColoradoDemography/coloradodemography.github.io.git && \  
cd coloradodemography.github.io && \  
jekyll build && \  
cd _site && \  
git clone https://github.com/ColoradoDemography/Control-Panel.git  
  
CMD ["node", "index.js"]

