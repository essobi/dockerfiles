FROM nginx:latest  
LABEL maintainer infrastructure@dallasmakerspace.org  
LABEL
traefik.frontend.rule=Host:demo.communitygrid.dallasmakerspace.org;Host:demo.communitygrid.dms.local  
LABEL traefik.enable=true  
LABEL traefik.port=80  
COPY src /usr/share/nginx/html  

