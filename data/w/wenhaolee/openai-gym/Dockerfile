FROM eboraas/openai-gym  
MAINTAINER Wen-Hao Lee <wing3s@gmail.com>  
  
RUN apt-get update && \  
/usr/local/bin/pip --no-cache-dir install pandas && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/* /root/.cache/pip/  
  
# Jupyter Notebook  
EXPOSE 8888  
# TensorBoard  
EXPOSE 6006  
WORKDIR /mnt/notebooks  
  
CMD ["/tmp/openai-gym.sh"]  

