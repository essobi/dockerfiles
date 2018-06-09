FROM nginx:alpine  
  
LABEL maintainer "Sebastian Tabares Amaya <sytabaresa@gmail.com>"  
  
# Install Git  
RUN apk -U --no-progress add git bash nodejs  
  
# NginX Configuration  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY mime.types /etc/nginx/mime.types  
COPY web-http.conf /etc/nginx/web-http.conf  
COPY web-https.conf /etc/nginx/web-https.conf  
  
WORKDIR /usr/local/taiga  
# Install taiga-front-dist  
RUN \  
git clone https://github.com/taigaio/taiga-front-dist.git taiga-front-dist &&
\  
cd taiga-front-dist && \  
git checkout stable  
  
# Github Oauth2 plugin support:  
RUN git clone https://github.com/taigaio/taiga-contrib-github-auth/ && \  
cd taiga-front-dist/dist && mkdir -p plugins && cd plugins && \  
ln -s ../../../taiga-contrib-github-auth/front/dist github-auth && \  
cd github-auth && npm install  
  
# Configuration and Start scripts  
COPY ./configure ./configure  
COPY ./start ./start  
#RUN chmod +x /usr/local/taiga/configure /usr/local/taiga/start  
EXPOSE 80 443  
ENTRYPOINT ["./configure"]  
CMD ["./start"]  

