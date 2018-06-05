FROM node:4.4.3  
  
RUN apt-get update \  
&& apt-get install -y ruby sudo \  
&& gem install dpl heroku-api rendezvous \  
&& wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh \  
&& heroku --version \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cp /etc/hosts /tmp/hosts  
RUN mkdir -p -- /lib-override && cp /lib/x86_64-linux-gnu/libnss_files.so.2
/lib-override  
RUN echo "10.1.4.67 gl.maps.utp.edu.co" >> /tmp/hosts  
RUN perl -pi -e 's:/etc/hosts:/tmp/hosts:g' /lib-override/libnss_files.so.2  
ENV LD_LIBRARY_PATH /lib-override  

