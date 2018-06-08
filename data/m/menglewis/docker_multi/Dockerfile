FROM python:2.7  
USER root  
  
# Install Tini  
RUN wget --quiet
https://github.com/krallin/tini/releases/download/v0.10.0/tini && \  
echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
WORKDIR /app  
  
COPY app.py /app  
COPY requirements.txt /app  
  
RUN pip install -r /app/requirements.txt  
  
ENTRYPOINT ["tini", "--"]  
CMD ["gunicorn", "-b", "0.0.0.0:8888", "app:app"]  

