FROM grihabor/research:cuda8-cudnn6  
MAINTAINER Borodin Gregory <grihabor@gmail.com>  
  
RUN pip3 install --no-cache-dir --upgrade pip \  
&& pip3 install --no-cache-dir jupyter  
  
WORKDIR /root  
  
CMD [ \  
"jupyter", \  
"notebook", \  
"--ip=0.0.0.0", \  
"--allow-root" \  
]  

