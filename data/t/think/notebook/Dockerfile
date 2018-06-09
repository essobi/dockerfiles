FROM alpine  
MAINTAINER think@hotmail.de  
  
# TODO: combine steps  
RUN \  
apk update && apk upgrade && \  
apk add --no-cache --virtual=build-dependencies gcc python3 python3-dev && \  
apk add --no-cache --virtual=ca-certificates glibc-dev musl-dev linux-headers
g++ wget && \  
apk add --no-cache musl-dev linux-headers g++ && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \  
pip3 install --no-cache-dir notebook ipywidgets && \  
apk add --no-cache --virtual=curl  
  
# RUN apk del build-dependencies gcc ca-certificates g++ python3-dev linux-
headers g++ glibc-dev  
RUN \  
# Notebook - TOC  
mkdir -p $(ipython locate)/profile_default/static/custom && \  
touch $(ipython locate)/profile_default/static/custom/custom.js && \  
touch $(ipython locate)/profile_default/static/custom/custom.css && \  
curl -L
https://rawgithub.com/minrk/ipython_extensions/master/nbextensions/toc.js >
$(ipython locate)/nbextensions/toc.js && \  
curl -L
https://rawgithub.com/minrk/ipython_extensions/master/nbextensions/toc.css >
$(ipython locate)/nbextensions/toc.css && \  
echo '$([IPython.events]).on("app_initialized.NotebookApp", function () {
IPython.load_extensions("toc"); });' >> $(ipython
locate)/profile_default/static/custom/custom.js && \  
echo 'require(["components/codemirror/addon/display/rulers"]); var clsname =
"ipynb_ruler"; var rulers = [{column: 79, className: clsname}, {column: 99,
className: clsname}]; IPython.Cell.options_default.cm_config.rulers = rulers;'
>> $(ipython locate)/profile_default/static/custom/custom.js  
  
RUN \  
# Notebook - Notify  
curl -L https://raw.github.com/sjpfenninger/ipython-
extensions/master/nbextensions/notify.js > $(ipython
locate)/nbextensions/notify.js && \  
echo '$([IPython.events]).on("app_initialized.NotebookApp", function () {
IPython.load_extensions('notify'); });' >> $(ipython
locate)/profile_default/static/custom/custom.js  
  
RUN \  
apk add --no-cache git && \  
mkdir -p ~/.jupyter && ipython profile create default && \  
git clone https://github.com/damianavila/RISE.git && \  
cd RISE && python3 setup.py install && cd .. && rm -rf RISE  
  
RUN \  
ipython install-nbextension https://raw.githubusercontent.com/ipython-
contrib/IPython-notebook-
extensions/master/nbextensions/usability/dragdrop/main.js  
  
ADD examples /notebook  
  
RUN apk add --no-cache --virtual=git  
  
RUN \  
git clone https://github.com/ipython/ipython.git /examples && \  
mv /examples/examples /notebook/examples && \  
rm -rf /examples  
  
RUN \  
pip install --no-cache-dir jupyter_dashboards && \  
jupyter dashboards install --user --symlink --overwrite && \  
jupyter dashboards activate  
  
RUN \  
git clone https://github.com/ipython/ipywidgets.git /examples && \  
mv /examples/examples /notebook/widget_examples && \  
rm -rf /examples  
  
ADD notebook /bin  
RUN chmod +x /bin/notebook  
WORKDIR /notebook  
  
ENTRYPOINT ["/bin/notebook"]  
CMD ["--ip", "0.0.0.0", "--NotebookApp.default_url=notebooks/Index.ipynb"]  

