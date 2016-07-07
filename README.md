# pyramid_tutorial

# Move to workspace
cd /work/workspace/

# Create git repo and pull
git clone https://github.com/hughy603/pyramid_tutorial
cd pyramid_tutorial

# Create and Set the profile
. setup_env

# Create and Activate Virtual Environment
pyvenv-3.5 --without-pip $VENV
source $VENV/bin/activate

#Fix Curl CA Certificates
#http://askubuntu.com/questions/646594/how-to-fix-ca-cert-issues-with-curl-in-ubuntu-14-04

# Install pip and setup tools
curl https://bootstrap.pypa.io/get-pip.py | python

#Create $VENV/bin/activate_this.py
# Add content in https://github.com/jmcantrell/vim-virtualenv/issues/45

# Install Pyramid
pip install "pyramid==1.7"

# Push to githup
git commit -a -m "Initialized Pyramid Environment"
git push origin master
