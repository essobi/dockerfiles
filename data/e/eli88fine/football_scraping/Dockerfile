#docker build -t eli88fine/eli-laura-kenny:historical-data-scraper .  
  
##### tag after building: docker tag historical-data-scraper eli88fine/eli-
laura-kenny:historical-data-scraper  
  
FROM python:3  
  
# WORKDIR /c/Users/gitRepos/football_scraping  
WORKDIR /usr/src  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
#CMD [ "python", "./hello_world.py" ]  
  
##### previously it used $PWD instead, but that didn't seem to be working  
# to run a single script: docker run -it --rm --name my-running-script -v
`pwd`:/usr/src/myapp -w /usr/src/myapp python:3 python hello_world.py  
  
#### NOTE, docker-toolbox must be used within a subdirectory of C:\Users in
order to mount volumes  
#### NOTE, in order to be able to write to hard drive, open Virtual Box, click
Settings, Shared Folders, Add C:\Users\gitRepos\football_scraping as
usr/src/football_scraping, with Auto-mount and Make Permanent checked  
  
  
### If VirtualBox is started in administrative mode and then the machine
inside there is used and a volume is mounted to the container, then it seems
to work. but copy/paste isn't working inside the VirtualBox  
  
  
  
### 6/2/18: Start VirtualBox in adimnistrator mode, start docker quickstart in
administrator mode, use this: docker run -it --rm --name my-running-script -v
/c/Users/gitRepos/football_scraping/output:/mnt -w /mnt eli88fine/eli-laura-
kenny:historical-data-scraper bash  
########## may not need to start virtual box in administrator mode, just the
docker quickstart  
### to run single script: docker run -it --rm --name my-running-script -v
/c/Users/gitRepos/football_scraping/output:/mnt -w /usr/src eli88fine/eli-
laura-kenny:historical-data-scraper python hello_world.py  
  
  
# to upload:  
#  
# docker login (if not already logged in during this session)  
# docker push eli88fine/eli-laura-kenny:historical-data-scraper

