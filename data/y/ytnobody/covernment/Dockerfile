FROM ytnobody/alpine-perl:latest  
MAINTAINER ytnobody <ytnobody@gmail.com>  
  
RUN git clone https://github.com/ytnobody/Covernment.git /opt/covernment  
  
WORKDIR /opt/covernment  
RUN cpanm -n --installdeps .  
RUN cpanm -n Server::Starter Starlet  
  
VOLUME /var/covernment  
ENV COVERNMENT_WORKDIR=/var/covernment  
  
EXPOSE 9210  
CMD start_server \  
\--port 9210 \  
\--interval=4 \  
\-- plackup \  
-s Starlet \  
\--max-workers=12 \  
\--timeout=30 \  
\--max-req-per-child=10000 \  
app.psgi  
  

