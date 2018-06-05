FROM python:3  
#WORKDIR /usr/src/app  
COPY . .  
RUN python3 app.py  
RUN git clone https://blackish-murderer:1q2w3e4r@github.com/blackish-
murderer/python.git  
WORKDIR /python  
RUN git config user.name "blackish-murderer"  
RUN git config user.email "blackish.murderer@gmail.com"  
RUN git config push.default matching  
RUN date -u > empty  
RUN git add empty  
RUN git commit -m "Update empty"  
RUN git pull https://blackish-murderer:1q2w3e4r@github.com/blackish-
murderer/python.git  
RUN git push --repo https://blackish-murderer:1q2w3e4r@github.com/blackish-
murderer/python.git  

