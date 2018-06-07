FROM openjdk:8-slim  
LABEL maintainer everpeace <https://github.com/everpeace/>  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get install -y lp-solve liblpsolve55-dev \  
&& cd /opt \  
&& wget
https://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.0.15/lp_solve_5.5.0.15_java.zip
\  
&& unzip lp_solve_5.5.0.15_java.zip && rm lp_solve_5.5.0.15_java.zip \  
&& apt-get remove --purge -y wget \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /opt \  
&& cp lp_solve_5.5_java/lib/ux64/liblpsolve55j.so /usr/lib/lp_solve \  
&& chmod 755 /usr/lib/lp_solve/liblpsolve55j.so  
  
ENV LD_LIBRARY_PATH /usr/lib/lp_solve  
# test  
ADD Test.java /tmp  
RUN cd /tmp && \  
javac -cp /opt/lp_solve_5.5_java/lib/lpsolve55j.jar Test.java && \  
java -cp ./:/opt/lp_solve_5.5_java/lib/lpsolve55j.jar Test && \  
rm /tmp/Test.java /tmp/Test.class  

