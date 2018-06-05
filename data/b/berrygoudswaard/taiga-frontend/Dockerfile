FROM nginx:1.10  
MAINTAINER Berry Goudswaard <berry@atom.nl>  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
git \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd -G sudo -d /home/taiga -m taiga \  
&& mkdir /home/taiga/logs \  
&& su taiga -c "cd ~ \  
&& git clone https://github.com/taigaio/taiga-front-dist.git taiga-front-dist
\  
&& cd taiga-front-dist \  
&& git checkout stable \  
&& cp /home/taiga/taiga-front-dist/dist/conf.example.json /home/taiga/taiga-
front-dist/dist/conf.json"  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["nginx"]  

