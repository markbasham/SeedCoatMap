Bootstrap: docker
From: continuumio/miniconda3
%files
./* ./

%post
# install browser
apt install --assume-yes chromium-browser

# install packages.
/opt/conda/bin/conda env create -f /enviroment.yml


%runscript
. /opt/conda/bin/activate main
exec /opt/conda/envs/main/bin/jupyter notebook --no-browser
#exec /opt/conda/envs/main/bin/python /src/seedcoatmap.py "$@"
