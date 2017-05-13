import pickle
import os 

dockerfiles = pickle.load(open('dockerfiles.pkl','rb'))

base = "%s/dockerfiles" %os.getcwd()
if not os.path.exists(base):
    os.mkdir(base)

for name,content in dockerfiles.items():
    # We will treat the user/organization as the entity
    entity,repo_name = name.split('/')
    entity_folder = "%s/%s" %(base,entity)
    text_folder = "%s/text" %entity_folder
    if not os.path.exists(entity_folder):
        os.mkdir(entity_folder)
        os.mkdir(text_folder)
    repo_folder = "%s/%s" %(text_folder,repo_name)
    if not os.path.exists(repo_folder):
        os.mkdir(repo_folder)
    dockerfile = "%s/Dockerfile" %(repo_folder)
    with open(dockerfile,'w') as filey:
        filey.writelines(content)


# Now let's use Singularity client to generate a manifest (metadata) for each
os.chdir('/home/vanessa/Documents/Dropbox/Code/singularity/singularity/libexec/python')
from singularity.utils import write_json

from docker.api import *
for name,content in dockerfiles.items():
    entity,repo_name = name.split('/')
    repo_folder = "%s/%s/text/%s" %(base,entity,repo_name)
    client = DockerApiConnection(image=name)
    manifestv1 = client.get_manifest(old_version=True)
    manifest = client.get_manifest()
    manifests = {'v1':manifestv1,
                 'v2':manifest}
    metadata_file = "%s/Dockerfile.json" %(repo_folder)
    write_json(manifests,metadata_file)

