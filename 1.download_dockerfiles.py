#!/usr/bin/env python

from sregistry.utils import write_file
from bs4 import BeautifulSoup
import html2text
import pickle
import requests
import os

# Load in the yuuge list of Docker images
containers = pickle.load(open('containers_2.pkl', 'rb'))

# Make a data folder
os.system('mkdir -p data')

start = 0
for c in range(start,len(containers)):

    container = containers[c]

    if '/' not in container:
        continue 

    collection,repo = container.split('/',1)
    dockerfile = None

    letter_dir = os.path.join('data', collection[0])
    collection_dir = os.path.join(letter_dir, collection)
    output_dir = os.path.join(collection_dir, repo)
    docker_file = '%s/Dockerfile' %output_dir

    if os.path.exists(docker_file):
        continue

    # Now look for the Dockerfile
    url = "https://hub.docker.com/r/%s/~/dockerfile/" %(container)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.select("span[class^=Dockerfile]")
        if len(text) > 0:
            text = str(text[0]).replace('\n','<br>')
            dockerfile = html2text.html2text(text)

            # Check for missing dockerfile
            if len(dockerfile.replace('\n','')) == 0:
                dockerfile = None            

    # If we have something, write it!
    if dockerfile is not None:

        print('Result for %s!' %(container))

        # Create the output directory, if doesn't exist
        for outdir in [letter_dir, collection_dir, output_dir]:
            if not os.path.exists(outdir):
                os.mkdir(outdir)

        # Dockerfile is text file
        if dockerfile is not None:
            write_file(docker_file, dockerfile)
