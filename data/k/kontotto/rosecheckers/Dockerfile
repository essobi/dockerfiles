FROM kontotto/rose:ubuntu14.04  
ENV ROSE=/usr/local  
ENV WORKSPACE=/srv  
ENV ROSECHK=$WORKSPACE/rosecheckers/rosecheckers  
WORKDIR $WORKSPACE  
  
# pre-install rose  
RUN git clone \--depth=1 https://github.com/kontotto/rosecheckers \  
&& cd $ROSECHK \  
&& make -j $(nproc) pgms \  
&& mv rosecheckers /usr/local/bin \  
&& rm -rf $WORKSPACE  

