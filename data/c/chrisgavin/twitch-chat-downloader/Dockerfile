FROM python:3.6  
RUN git clone "https://github.com/PetterKraabol/Twitch-Chat-Downloader.git"
"/src/" && \  
mkdir /config/ && \  
ln -s "/config/settings.json" "/src/settings.json" && \  
pip install -r "/src/requirements.txt"  
WORKDIR "/src/"  
ENTRYPOINT ["python3", "./app.py", "--output", "/mnt/", "-v"]  

