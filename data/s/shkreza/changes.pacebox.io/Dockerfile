FROM shkreza/base.pacebox.io:v0.1  
  
LABEL vendor="Pacebox.io"  
# apt-get udpate  
# apt-get install lsb-release  
# export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"  
# echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee
-a /etc/apt/sources.list.d/google-cloud-sdk.list  
# curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
# apt-get install google-cloud-sdk-app-engine-python -y  
  
COPY . /server  
ENV PYTHONPATH /server  
ENV GOOGLE_APPLICATION_CREDENTIALS
/secrets/googlesecrets/pacebox1-serviceaccount.json  
  
CMD ["python", "/server/traveltime.py"]  
  
EXPOSE 5000  

