FROM sys42/docker-build-essentials:1.0.0  
MAINTAINER Tom Nussbaumer <thomas.nussbaumer@gmx.net>  
COPY _internal_ /  
RUN chmod +x _internal_ && sudo -iu app /_internal_ && rm _internal_  

