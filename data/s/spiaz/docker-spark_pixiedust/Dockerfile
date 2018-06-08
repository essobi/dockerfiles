FROM spiaz/docker-spark2.1:latest  
  
LABEL maintainer="Stefano Piazza"  
  
# Set working directory in /  
WORKDIR /app  
  
# Add and install requirements  
ADD requirements.txt /app/requirements.txt  
RUN pip3 --no-cache-dir install -r requirements.txt  
  
# Install pixiedust (for %%scala magic cell in jupyter)  
RUN pip3 install pixiedust &&\  
mkdir -p /root/pixiedust/bin &&\  
jupyter pixiedust install --silent --spark=2.1.0  
  
EXPOSE 8888  
VOLUME /app  
  
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", \  
"--allow-root"]  

