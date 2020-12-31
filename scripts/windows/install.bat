@REM You must have Anaconda installed and activated for this to work

cd ../../ && conda create --name discord-friends --file requirements.txt python=3.7
conda activate discord-friends && cd scripts/windows && setup.bat