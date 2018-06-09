FROM aldryn/base-project:py3-3.15  
ENV PYTHONPATH /app/src:$PYTHONPATH  
  
COPY stack/imageopt /stack/imageopt  
RUN /stack/imageopt/install.sh  
  
COPY stack/moviepy /stack/moviepy  
RUN /stack/moviepy/install.sh  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.2.1  
COPY stack/node /stack/node  
RUN /stack/node/install.sh  
  
## node modules  
## ------------  
ENV PATH=/app/node_modules/.bin:$PATH  
COPY package.json /app/package.json  
RUN npm install  
  
# python requirements  
# -------------------  
ENV PIP_INDEX_URL=https://wheels.aldryn.net/d/pypi/aldryn-baseproject-py3/\  
PIP_EXTRA_INDEX_URL=https://devpi.divio.ch/aldryn/extras/+simple/\  
PIP_RETRIES=12  
COPY requirements.txt /app/  
RUN pip install --no-deps -r requirements.txt  
RUN python -c "from imageio.plugins import avbin; avbin.get_avbin_lib()"  
RUN python -c "from imageio.plugins import _freeimage;
_freeimage.get_freeimage_lib()"  
RUN python -c "from imageio.plugins import ffmpeg; ffmpeg.get_exe()"  
  
COPY . /app  
# gzip does not seem to work with python3 yet  
ENV DISABLE_GZIP=True  
RUN DJANGO_MODE=build python manage.py graphql_schema  
RUN npm run build-production  
RUN DJANGO_MODE=build python manage.py collectstatic --noinput  

