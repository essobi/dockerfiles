FROM bamdad/jdk8-gradle  
  
RUN apt-get update  
  
RUN apt-get install -y curl bzip2  
  
RUN curl -L https://aphyr.com/riemann/riemann-0.2.10.tar.bz2 -o
/tmp/riemann.tar.bz2  
RUN tar xvfj /tmp/riemann.tar.bz2 -C /opt  

