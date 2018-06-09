FROM nginx  
  
MAINTAINER PhuongNL "phuongnl.hn@gmail.com"  
# Install NodeJS  
RUN apt-get update \  
&& apt-get install -y curl \  
&& apt-get install -y build-essential \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Strong Nginx  
RUN npm install -g strong-nginx-controller \  
&& npm cache clear  
  
EXPOSE 80 443  
ENTRYPOINT ["sl-nginx-ctl", "-c", "http://0.0.0.0:8801", "-l",
"http://0.0.0.0:80"]  

