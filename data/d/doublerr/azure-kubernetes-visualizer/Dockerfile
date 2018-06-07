FROM dockerfile/nodejs:latest  
  
RUN mkdir /opt/kubernetes-visualizer  
ADD . /opt/kubernetes-visualizer  
  
EXPOSE 3000  
WORKDIR /opt/kubernetes-visualizer  
  
RUN npm install socket.io cli express flavored-path  
  
ENV KUBESERVER 127.0.0.1:8080  
ENV NUMMINIONS 4  
ENV KUBEAUTHUSER admin  
ENV KUBEAUTHPASSWORD foo  
  
RUN chmod +x index.js  
  
ENTRYPOINT ./index.js -s $KUBESERVER -m $NUMMINIONS -a $KUBEAUTHUSER -x
$KUBEAUTHPASSWORD  

