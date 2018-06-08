FROM continuumio/anaconda3  
LABEL maintainer c.sachs@fz-juelich.de  
RUN apt-get update && apt-get install -y unzip libgl1-mesa-glx && \  
# opengl for qt...  
apt-get clean && \  
conda config \--add channels conda-forge && \  
conda config \--add channels bioconda && \  
conda config \--add channels csachs && \  
conda install -y mycelyso mycelyso-inspector && \  
pip uninstall -y mycelyso && \  
pip install "git+https://github.com/modsim/mycelyso#egg=mycelyso" && \  
adduser \--disabled-password user && \  
mkdir /data /examples && \  
wget https://github.com/modsim/mycelyso/archive/master.zip -O
/tmp/mycelyso.zip && \  
unzip -j /tmp/mycelyso.zip 'mycelyso-master/examples/*' -d /examples && \  
rm /tmp/mycelyso.zip && \  
apt-get remove -y unzip && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
ln -s /examples /home/user && \  
chown -R user:user /data /examples /home/user && \  
runuser user -s /bin/sh "-c jupyter notebook --generate-config" && \  
echo "c.NotebookApp.ip = '0.0.0.0'" >>
/home/user/.jupyter/jupyter_notebook_config.py && \  
echo "c.NotebookApp.notebook_dir = '/home/user'" >>
/home/user/.jupyter/jupyter_notebook_config.py && \  
echo Done  
  
USER user  
  
WORKDIR /data  
  
EXPOSE 8888  
  
ENTRYPOINT ["python", "-m", "mycelyso"]  

