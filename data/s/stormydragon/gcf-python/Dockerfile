FROM python AS py_build  
  
WORKDIR /app  
ENV PYENV_ROOT="/app/pyenv" \  
PATH="$PYENV_ROOT/bin:$PATH"  
RUN git clone https://github.com/pyenv/pyenv.git pyenv \  
&& ./pyenv/bin/pyenv install 3.6.5 \  
&& ./pyenv/versions/3.6.5/bin/python -m pip install --upgrade pipenv pip \  
&& rm -rf `find -type d -name __pycache__` \  
&& rm -rf ./pyenv/versions/3.6.5/lib/python3.6/test  
COPY cloud_func/Pipfile cloud_func/Pipfile.lock ./  
RUN ./pyenv/versions/3.6.5/bin/python -m pipenv lock --requirements >
requirements.txt \  
&& ./pyenv/versions/3.6.5/bin/python -m pip install -r requirements.txt  
  
FROM gcr.io/google-appengine/nodejs as final  
RUN install_node v6.11.5 \  
&& apt-get update \  
&& apt-get install -y zip \  
&& export CLOUD_SDK_REPO="cloud-sdk-jessie" \  
&& echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee
-a /etc/apt/sources.list.d/google-cloud-sdk.list \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
\  
&& apt-get update -y && apt-get install google-cloud-sdk -y  
WORKDIR /tmp/cloud_worker  
COPY google_cloud_worker/yarn.lock google_cloud_worker/package.json ./  
RUN yarn install  
COPY google_cloud_worker/worker.js ./  
WORKDIR /app  
COPY cloud_func/package.json cloud_func/yarn.lock ./  
RUN yarn install  
COPY cloud_func ./  
COPY \--from=py_build /app/pyenv/versions/3.6.5 /app/python  
ENV PATH="/app/python/bin:$PATH" \  
PYTHONPATH="/app/python" \  
PYTHONHOME="/app/python" \  
LC_ALL="C.UTF-8" \  
LANG="C.UTF-8"  
RUN zip -9 -ur package.zip .  
COPY deployer /deployer  
  
ONBUILD COPY Pipfile Pipfile.lock ./  
ONBUILD RUN python -m pipenv lock --requirements > requirements.txt \  
&& python -m pip install -r requirements.txt  
ONBUILD COPY . ./user_code  
ONBUILD RUN zip -9 -ur package.zip .  
  
ENV GOOGLE_APPLICATION_CREDENTIALS=/service-account.json  
ENTRYPOINT ["python", "/deployer/deploy.py", "--package=package.zip"]  

