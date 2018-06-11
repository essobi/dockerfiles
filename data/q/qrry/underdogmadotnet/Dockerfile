FROM nginx:latest  
  
RUN echo 'deb [trusted=yes]
"http://storage.googleapis.com/download.dartlang.org/linux/debian" stable
main' > /etc/apt/sources.list.d/googleapis.list  
RUN apt-get update -y  
RUN apt-get install -y dart git make  
RUN mkdir -p /opt/underdogmadotnet  
RUN git clone https://github.com/querry43/underdogmadotnet.git
/opt/underdogmadotnet  
RUN make -C /opt/underdogmadotnet  
RUN rm -rf /usr/share/nginx/html  
RUN ln -s /opt/underdogmadotnet/build/web /usr/share/nginx/html  
  
EXPOSE 80  

