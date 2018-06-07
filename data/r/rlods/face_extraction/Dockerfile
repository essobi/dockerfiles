FROM rudyryk/alpine-opencv  
  
COPY haarcascade_frontalface_alt.xml /app/  
COPY main.py /app/  
WORKDIR /app  
  
ENTRYPOINT [ "python3", "main.py" ]  

